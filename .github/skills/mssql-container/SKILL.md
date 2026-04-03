---
name: mssql-container
description: "Manage the local MSSQL Server running in a container (Podman/Docker). Use when: resetting the database, restoring from backup, recreating the SQL Server container, fresh database setup, executing SQL queries, backing up the database, generating/exporting a database backup, listing backup files in the container, or running ad-hoc queries against the Accounting database."
argument-hint: "Mode: default (restore only), 'full reset' (recreate container + restore), 'list files' (show backups in container), or 'backup' (export .bak — filename required). Optional: backup filename, SA password."
---

# Manage Local MSSQL Server

Manages the local SQL Server container: restore a database from backup, fully recreate the container, execute queries, or generate a new backup.

## Modes

| Mode | Trigger | What it does |
|------|---------|--------------|
| **Default** (restore) | No special keyword | Restores the Accounting database from the `.bak` already inside the container (Steps 4–5) |
| **Full reset** | User says "full reset" or "full" | Tears down the container, starts a fresh one, copies the backup in, restores, and verifies (Steps 1–5) |
| **List files** | User says "list", "list files", or "what backups" | Lists available files inside the container's `/var/opt/mssql/` directory (Step 0) |
| **Backup** | User says "backup", "export", or "generate backup" | Backs up the current Accounting database inside the container and copies the `.bak` to a local file (Step 6). **Requires a filename.** |

## Parameters

The user may provide these values. If not specified, use the defaults:

| Parameter | Default | Description |
|-----------|---------|-------------|
| Backup file | `AccountingLinux.bak` | The `.bak` file in the workspace root (source for restore, or destination for backup) |
| SA password | `IGTtest1` | The SQL Server SA password for the new container |

## Allowed Tools

This skill should **only** use the following tools. Do not use any other tools.

- `run_in_terminal` — Container runtime commands (stop, rm, run, cp, exec)
- `mssql_list_servers` — Discover available SQL Server connections
- `mssql_connect` — Connect to the SQL Server instance
- `mssql_run_query` — Execute SQL queries (RESTORE, BACKUP, SELECT)
- `mssql_change_database` — Switch to a database

---

## Container Runtime

The `<runtime>` placeholder in all commands below refers to the container runtime CLI:

| OS | Default runtime | Command |
|----|----------------|--------|
| **Windows** | Podman | `podman` |
| **Linux / macOS** | Docker | `docker` |

Both Docker and Podman use identical CLI syntax for the commands in this skill (`run`, `stop`, `rm`, `cp`, `exec`). Detect the OS and use the appropriate default. If the user explicitly requests a different runtime, honour that.

---

## List Files (Step 0)

List the backup files available inside the running container:

```sh
<runtime> exec sql ls -lh /var/opt/mssql/
```

Show the output to the user. This is useful to check which `.bak` files are already present before restoring.

---

## Full Reset Steps (Steps 1–5)

> **Default mode** skips to Step 4 directly (the container and `.bak` file must already be in place).
>
> **Full reset mode** executes all steps 1 through 5.

### Step 1 — Stop and remove existing container

Remove any previous `sql` container. Ignore errors if it doesn't exist.

```sh
<runtime> stop sql 2>/dev/null; <runtime> rm sql 2>/dev/null; echo "Old container removed (or was not running)"
```

### Step 2 — Start a fresh SQL Server container

```sh
<runtime> run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=<password>" -e "MSSQL_PID=Developer" -p 1433:1433 -d --name=sql mcr.microsoft.com/mssql/server:2022-latest
```

Replace `<password>` with the user-provided SA password.

After starting, **wait for SQL Server to finish initializing** by polling until it accepts connections (retry every 2 seconds, up to ~60 seconds):

```sh
until <runtime> exec sql /opt/mssql-tools18/bin/sqlcmd -S localhost -U SA -P "<password>" -C -Q "SELECT 1" &>/dev/null; do sleep 2; done
```

### Step 3 — Copy the backup file into the container

```sh
<runtime> cp <backup-file> sql:/var/opt/mssql/<backup-file>
```

Replace `<backup-file>` with the user-provided `.bak` filename.

Then fix permissions so the `mssql` process inside the container can read the file:

```sh
<runtime> exec --user root sql chmod 644 /var/opt/mssql/<backup-file>
```

### Step 4 — Restore the database

Use the **MSSQL MCP server** tools to restore the database:

1. Call `mssql_list_servers` to get the server name (expect `localhost` or `127.0.0.1,1433`).
2. Call `mssql_connect` with the server name and **no** database (connect to default/master).
3. Call `mssql_run_query` with this SQL (substitute the actual database name and backup filename):

```sql
ALTER DATABASE <database-name> SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
RESTORE DATABASE <database-name>
FROM DISK = '/var/opt/mssql/<backup-file>'
WITH REPLACE;
```

The `ALTER DATABASE` line drops any active connections before restoring. It will fail harmlessly if the database doesn't exist yet (e.g. first-time restore on a fresh container) — the `RESTORE` will still succeed.

Use `queryTypes: ["ALTER", "RESTORE"]` and `queryIntent: "backup_restore"`.

> **If the backup was made on Windows**, the embedded file paths will be Windows paths (e.g. `C:\Program Files\Microsoft SQL Server\...`) and the plain `RESTORE` above will fail. Use **Step 4W** instead.

---

### Step 4W — Restore a Windows backup (MOVE required)

Use this variant when the `.bak` was created on a Windows SQL Server instance. The backup contains Windows-style physical paths that must be remapped to Linux paths via `WITH MOVE`.

#### Step 4W-a — Discover logical file names

Call `mssql_run_query` against `master`:

```sql
RESTORE FILELISTONLY
FROM DISK = '/var/opt/mssql/<backup-file>';
```

Use `queryTypes: ["RESTORE"]` and `queryIntent: "backup_restore"`.

The result is a table with one row per file in the backup. Note the `LogicalName` value for each row:
- The row where `Type = 'D'` is the data file (`.mdf`).
- The row where `Type = 'L'` is the log file (`.ldf`).

There may be additional `Type = 'S'` filestream rows — add a `MOVE` clause for each one as well.

> **Important**: Read the `LogicalName` and `Type` values directly from the `mssql_run_query` tool's response. Do **not** run any terminal or PowerShell commands to parse the result file. The tool returns the data inline — extract the values from its output and proceed immediately to Step 4W-b.

#### Step 4W-b — Restore with MOVE

Call `mssql_run_query` using the logical names discovered above:

```sql
ALTER DATABASE <database-name> SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
RESTORE DATABASE <database-name>
FROM DISK = '/var/opt/mssql/<backup-file>'
WITH REPLACE,
     MOVE '<logical-data-name>' TO '/var/opt/mssql/data/<database-name>.mdf',
     MOVE '<logical-log-name>'  TO '/var/opt/mssql/data/<database-name>_log.ldf';
```

Replace `<logical-data-name>` and `<logical-log-name>` with the `LogicalName` values from Step 4W-a.

Use `queryTypes: ["ALTER", "RESTORE"]` and `queryIntent: "backup_restore"`.

The `ALTER DATABASE` line will fail harmlessly on a fresh container where the database does not yet exist — the `RESTORE` will still succeed.

### Step 5 — Verify the restore

After the restore completes, verify it succeeded:

1. Call `mssql_change_database` to switch to the restored database.
2. Run a verification query:

```sql
SELECT
    DB_NAME() AS [Database],
    DATABASEPROPERTYEX(DB_NAME(), 'Status') AS [Status],
    (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE') AS [TableCount]
```

Use `queryTypes: ["SELECT"]` and `queryIntent: "testing_validation"`.

**Expected result**: Database = `<database-name>`, Status = `ONLINE`, TableCount > 0.

Report the verification results to the user.

---

## Backup Mode (Step 6)

Use this when the user wants to **export** a database to a `.bak` file.

> **All parameters are mandatory.** If the user did not provide the database name, output filename, or SA password, **ask before proceeding**.

### Step 6a — Generate backup inside the container

1. Call `mssql_list_servers` to get the server name.
2. Call `mssql_connect` with the server name (connect to master).
3. Call `mssql_run_query` with this SQL (substitute the actual database name):

```sql
BACKUP DATABASE <database-name>
TO DISK = '/var/opt/mssql/<database-name>_export.bak'
WITH FORMAT, INIT, COMPRESSION;
```

Use `queryTypes: ["BACKUP"]` and `queryIntent: "backup_restore"`.

### Step 6b — Copy the backup file out of the container

```sh
<runtime> cp sql:/var/opt/mssql/<database-name>_export.bak <backup-file>
```

Replace `<backup-file>` with the **user-provided** local filename.

### Step 6c — Verify the backup file

```sh
ls -lh <backup-file>
```

Report the file size to the user to confirm the backup was created successfully.

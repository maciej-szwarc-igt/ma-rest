# Chapter 6 Maintenance Console

The Maintenance Console is used to create and edit reference data pertaining to casino machines, including cabinet types, sections, game types, display types, manufacturers, denominations, and machine types.

## 6.1 Cabinet Types

Cabinet types categorize the physical form factor of machines at the property.

### Managing Cabinet Types

- **Add** — Provide the name of the new cabinet type.
- **Modify** — Update the name of an existing cabinet type.
- **Delete** — Remove a cabinet type. A cabinet type cannot be deleted if it is referenced by a machine.

> Deletion is immediate with no confirmation. Always verify the correct item is selected before deleting.

## 6.2 Sections

Sections represent areas of the casino floor.

### Managing Sections

- **Add** — Provide up to four alphanumeric characters for the section name.
- **Modify** — Update the section name.
- **Delete** — Remove a section. A section cannot be deleted if it is referenced by a machine.

> Deletion is immediate with no confirmation.

## 6.3 Game Types

Game types categorize the types of games available at the property.

### Managing Game Types

- **Add** — Provide the name of the new game type.
- **Modify** — Update the game type name.
- **Delete** — Remove a game type. A game type cannot be deleted if referenced by another table.

> Deletion is immediate with no confirmation.

## 6.4 Display Types

Display types categorize the display technology of machines.

### Managing Display Types

- **Add** — Provide the name of the new display type.
- **Modify** — Update the display type name.
- **Delete** — Remove a display type. A display type cannot be deleted if in use.

> Deletion is immediate with no confirmation.

## 6.5 Manufacturers

Manufacturers identify the maker of each machine.

### Managing Manufacturers

- **Add** — Provide the manufacturer's name.
- **Modify** — Update the manufacturer's name.
- **Delete** — Remove a manufacturer. A manufacturer cannot be deleted if in use.

> Deletion is immediate with no confirmation.

## 6.6 Denominations

Denominations define the coin/credit denominations used at the property.

Each denomination record includes:

| Field | Description |
|-------|-------------|
| Denom ID | Unique identifier |
| Denom | Denomination value (e.g., 0.01, 0.05, 0.25) |
| Hard Drop Variance | Hard drop variance threshold for this denomination |
| Soft Drop Variance | Soft drop variance threshold for this denomination |
| Beginning Range | Starting machine number range for the denomination |
| End Range | Ending machine number range for the denomination |

### Managing Denominations

- **Add** — Provide the denomination value and configure variance thresholds and machine number ranges.
- **Modify** — Update denomination settings.
- **Delete** — Remove a denomination (only if not in use).

## 6.7 Machine Types

Machine types define the configuration profile for groups of similar machines on the floor. Each machine type includes:

| Field | Description |
|-------|-------------|
| Type ID | Unique identifier |
| Description | Brief description of the machine type |
| Par (Hold %) | Theoretical hold percentage |
| Denom | Base denomination |
| Max Bet | Maximum bet per play |
| Lines | Number of lines available |
| Credits/Points | Maximum credits/points per line |
| Manufacturer | Machine manufacturer |
| Tolerance | Meter tolerance for this type |
| XCPlayPercent | Xtra Credit play percentage (if XC Reporting enabled) |

### Managing Machine Types

- **Add** — Create a new machine type with all required fields.
- **Modify** — Update machine type settings.
- **Delete** — Remove a machine type (only if no machines reference it).

## 6.8 Comments

The Maintenance Console also manages pre-defined comments (reasons) used throughout Machine Accounting for documenting actions such as variance acceptance, hand pay voids, and meter adjustments.

### Managing Comments

- **Add** — Create a new comment with a code and description.
- **Modify** — Update the comment text.
- **Delete** — Remove a comment.

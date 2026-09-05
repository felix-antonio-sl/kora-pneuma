---
urn: urn:fxsl:kb:opcloud-tutorial-videos
nombre: opcloud-tutorial-videos
version: 1.0.0
estado: borrador
descripcion: "Guia tutorial de OPCloud en una serie de 50 videos; evidencia pedagogica, no canon OPM"
fuente: "Fuente externa opcloud videos, archivada en kora-external-sources/_archivo/2026-08-03-fxsl-legacy-reviewed/fxsl/opm-methodology/opcloud-tutorial-videos.md (sha256:2b8e132df845ee9a908e961f15748910671088a80f1e48c4098561fb647adb6e); manifiesto original creado por kora/curator el 2026-03-12"
autor: kora-curator
creado: 2026-03-12
lang: en
tags: [opcloud, opm, tutorial, modelado, youtube, video-course]
familia: bok
---
# OPCloud Tutorial Videos

## Alcance de la fuente

- Serie tutorial de 50 videos.
- Clasificación de origen: tutorial; este artefacto es evidencia de uso de OPCloud y no modifica el canon OPM de KORA.


Comprehensive guide to Object-Process Methodology (OPM) modeling in OPCloud. Covers fundamental concepts, advanced features, simulation, and integration capabilities.

This tutorial series uses the OnStar system as the primary example throughout the course. The OnStar model demonstrates emergency assistance, GPS navigation, cellular communication, and advisor interaction workflows.


## Getting Started

### Creating Objects and Processes

- **Create Process**:
  1. Click process button in main toolbar (blue ribbon)
  2. Drag to canvas (OPD area)
  3. Enter name in popup text box
  4. Click update or press Enter to confirm
- **Create Object**:
  1. Click object button in main toolbar
  2. Drag to canvas
  3. Enter name in popup
  4. Click update or press Enter
- **Auto Format**: Toggle checkbox to auto-capitalize each word; disable for custom naming (e.g., "onstar" instead of "OnStar")
- **Connect Elements**: Click empty area (non-text), drag to target element to create link
- **Auto Capitalization**: Default behavior capitalizes first letter of each word

### Saving and Loading Models

- **Main Toolbar Buttons**:
  - Undo: Revert last action
  - Redo: Restore undone action
  - Save: Quick save to current location
  - Load: Open model browser
  - Share: Generate shareable link
  - Execution: Open simulation/execution mode
- **Main Menu Options**:
  - Create new model: Start fresh model
  - Load model: Open from storage
  - Load examples:
    - Global examples: Available to all OPCloud users
    - Organizational examples: Created by organization admin
- **Save Options**:
  - Quick save: Save to current location
  - Save as: Save to new location or rename
- **Model Options**:
  - System map: Visual overview of all OPDs
  - Copy link: Generate shareable model link
  - Model validation: Validate computational values and ranges
  - Compare models: Compare two model versions
  - Mark things: Color-code elements for team visibility
- **Auto Save**: Models automatically save when switching between tabs
- **Unsaved Indicator**: Tab shows "not saved" until first save

### Model Navigation

- **OPD Navigator**: Left pane tree view showing all diagrams in model
- **Draggable Things**: Panel showing all elements with type indicators:
  - Informational (i): Abstract data, calls, messages
  - Physical (P): Tangible objects, devices
  - Environmental (E): External factors, drivers
  - Systemic (S): Control systems
- **Connected Things**: Attributes shown connected to parent elements (e.g., danger status with driver)
- **Zoom**:
  - Zoom in: Make diagram larger
  - Zoom out: Make diagram smaller
  - Drag: Reposition view
- **Keyboard Shortcuts**:
  - Ctrl+Up: Navigate to parent OPD in tree
  - Ctrl+Down: Navigate to child OPD in tree
- **Drag and Drop**: Drag elements from draggable thing directly to canvas

### Model Wizard

- **Access**: Main Menu > New Model by Wizard
- **Purpose**: Guide new OPM users through model creation step-by-step
- **Stage Count**: 12 sequential stages
- **Coverage**: Not all OPCloud options; focuses on OPM methodology essentials
- **Example Model**: OnStar system (similar to Examples but with guidance)
- **Help Features**: Hover hints, assistant tooltips on bold items
- **Starting Point**: Creates System Diagram as top-level entry point
- **Limitations**: Not all features covered; manual extension required after completion
- **Workflow**: User defines motivation, system process, input/output/beneficiaries, connections


## Core Features

### OPD3 and Diagram Management

- **Create OPD**: Auto-generated when using in-zoom or unfold on element
- **OPD Naming Convention**:
  - SD: System Diagram (top level)
  - SD1: First child diagram
  - SD1.1: Child of SD1
  - SD1.1.1: Grandchild of SD1
- **Delete OPD**:
  - Only leaf nodes deletable (no children)
  - Inner nodes protected to maintain tree integrity
  - Error message for inner node deletion attempts
- **Expand/Collapse**:
  - Right-click menu for options
  - Expand all: Show entire tree
  - Collapse all: Hide all children
  - Hide names: Show only OPD numbers
  - Show names: Display full OPD names
- **Partial Expansion**: Models >20 OPDs show only current level expanded by default
- **Right-Click Menu**: Remove, expand all, collapse all, hide/show names

### Searching Elements

- **Search Tool**: Secondary toolbar search button opens model search
- **Filter Options**:
  - All elements
  - Processes only
  - Objects only
- **Search Input**: Type name to filter matching elements
- **Results**: Shows all elements containing search term
- **Location Column**: Shows OPD where element exists
- **Navigation**: Click location to switch to specific OPD and focus on element
- **Draggable Thing Search**: Right-click element name in draggable thing to filter

### Objects and Processes

- **Essence Types**:
  - Physical: Tangible things (cars, devices)
  - Informational: Abstract data, call records, messages
  - Environmental: External factors (weather, drivers)
  - Systemic: Systems that control or coordinate
- **Change Essence**: Secondary toolbar > change essence button
- **Description**: Add text, URLs, notes via double-click
- **URL Links**: Add via entities extension > view URL (images, videos, articles)
- **Unfold**: View sub-components (creates child OPDs)
- **Fold**: Collapse to compact view (bold contour indicator)
- **Update Button**: Confirm changes after editing names
- **Auto Format Toggle**: Control capitalization (OnStar vs onstar)
- **Inside Objects**: Objects created inside in-zoom processes
- **Outside Objects**: Objects created at system diagram level

### States

- **Add States**: Click halo > add states OR secondary toolbar add state button
- **Default Naming**: state1, state2 (lowercase, left to right)
- **State Links**: Effect link or in-out link pairs
- **Exchange Symbol**: Toggle between effect and in-out link
- **State Examples**: "requested call", "online" for call object
- **Update Behavior**: Clicking update advances to next state name automatically
- **Conditional Transitions**: Connect states to processes via instrument-condition links
- **Multiple States**: Add additional states by clicking add state button repeatedly

### Links and Connections

- **Link Types**: Structural (exhibition/characterization), Instrumental, Consumption, Effect
- **Create Link**: Right-click source, drag to destination
- **Link Table**: Configure link properties, multiplicity, tags
- **Multiplicity**: Define number of objects required (e.g., "2 drivers")
- **Path**: Conditional paths (e.g., different cars for different routes)
- **Agent Links**: Connect human agents to processes
- **Instance Links**: Create specific instances of objects
- **Visual Instances**: Same logical entity with different visual representation
  - **Creation**: Use "use existing thing" option when naming conflict occurs
  - **Restriction**: Cannot create visual instance between different element types (e.g., object to process)
  - **Use Case**: Same entity appears in multiple OPDs with different visual context
  - **vs Logical Instance**: Visual = same thing different view; Logical = inheritance relationship
- **Specialization**: Generalization relationships between objects

### Link Properties

- **Access**: Right-click link > properties
- **Properties**: Source multiplicity, target multiplicity, tag, path probability, style
- **Link Style**: Color (hex), width, copy style to other links

### Advanced OPL Panel

- **Shift Pane**: Move OPL panel to left side using button
- **Toggle Numbering**: Enable/disable line numbers in OPL view
- **Minimize Panel**: Stop rendering OPL for cleaner OPD workspace
- **Purpose**: Improve performance on crowded diagrams
- **Manual Editing**: Direct OPL script modification available

### Touch Screen Support

- **Long Press**: Alternative to right-click on touch devices
- **Gesture Navigation**: Touch-based OPD navigation supported
- **Reference**: User manual for complete gesture list

### Inner and Outer Objects

- **Inner Objects**:
  - Created inside in-zoom processes
  - Exist only within process scope
  - Cannot exist outside parent process
  - Deleted when parent process deleted
- **Outer Objects**:
  - Created at system diagram level
  - Can be referenced in multiple OPDs
  - Exist independently of any single process
- **Conversion Methods**:
  - Delete and recreate inside/outside
  - Copy from draggable thing into target location
- **Drag Behavior**: Warning message when trying to drag outer object inside
- **Enveloping**: Process enlargement can "swallow" outer objects (appears inside but reverts when moved)
- **Visual Indicator**: Inner objects show inside-process notation


## Advanced Features

### Halo and Quick Commands

- **Access**: Click element to show halo (three dots near selection)
- **Unfold/In-Zoom**: Navigate to existing OPD or create new diagram
- **Convert to Computational**: Change process type for calculations
- **Delete**: Remove element with instance handling options
  - Multiple instances: Shows all instances for selection
  - Single instance: Removes directly
- **Time Duration**: Set process duration for exception links
- **Style Element**: Quick styling access for visual customization
- **Bring Connected**: Load related elements from other OPDs
- **Secondary Toolbar**: Same options available on toolbar for accessibility

### Semi-Folding

- **Purpose**: View object parts without overcrowding diagram
- **Activation**: Select object > semi-folded view option
- **Compact View**: Shows part names inside object container
- **Extract Part**: Double-click specific part to bring to main diagram
- **Missing Parts Indicator**: Number showing hidden parts in link (e.g., "2 more")
- **Restore**: Click link icon to return parts to semi-folded view
- **vs Full Unfold**: Semi-folded shows names; full unfold shows full details

### Text and Style

- **Style Options**:
  - Reset: Return to default styling
  - Font Size: Smaller or larger (via setting menu)
  - Font Family: Change typeface
  - Text Color: Custom color picker
  - Border: Element border styling
  - Alignment: Left, center, right
- **Manual Positioning**: Control X/Y axis for precise text placement
- **Position Presets**: Up, down, left, right, center options
- **Link Style**: Right-click link > style > color (hex code), width
- **Copy Style**: Copy link style and apply to other links
- **Reset Text Position**: Close manual positioning to reset

### Resizing and Auto-Size

- **Default Size**: OPCloud has minimum size for objects and processes
- **Fit to Text**: Entities extension > shrink to text
  - Automatically shrinks element to fit text
  - Maintains auto-resizing (will revert if text changes)
- **Toggle Auto-Sizing**: Entities extension > toggle auto-resizing
  - Disable to freely resize manually
  - Re-enable to return to automatic sizing
- **Manual Sizing**:
  - Make longer, narrower, or custom shapes
  - Cannot type beyond element bounds when auto-sizing disabled
  - Text remains visible when typing
- **Toggle Back**: Re-enable auto-sizing in entities extension

### Grid Feature

- **Activation**: Secondary toolbar > grid option button
- **Default State**: Off (must enable manually)
- **Settings**:
  - Grid on/off toggle
  - Size: Movement increment in pixels (default: 5)
  - Color: Grid line color
  - Thickness: Line thickness (higher = thicker)
  - Scale Factor: Lines visible (higher = fewer lines, lower = more lines)
- **Purpose**: Align elements, especially important for in-zoom process ordering
- **Process Order**: In-zoom process height/level determines execution order in OPM
- **Example**: Set size=5 for 5-pixel movement increments

### Images in Things

- **Image Sources**:
  - URL: External image link (must end with .jpeg, .png, etc.)
  - Heading Pool: Internal OPCloud image library
  - OPD Capture: Screenshot of current diagram
- **URL Requirements**: Must end with image extension (.jpg, .jpeg, .png, .gif)
- **Display Options**:
  - Show both text and image simultaneously
  - Toggle between text-only and image-only
- **Edit Mode**: Right-click to toggle view
- **Camera Icon**: Indicates embedded image in element
- **Multiple Images**: Cycle through with multiple clicks
- **Preview**: Check image before embedding


## Model Management

### Export Options

- **Export OPL**: Generate OPL text, with/without numbering
- **Export OPD as Image**:
  - Formats: JPEG, GIF
  - Resolution: 100 DPI (default), 300 DPI (high quality)
  - Scope: Current OPD, entire OPD tree, or system diagram only
  - Tooltip Display: Show computational process tooltips in export
- **Export PDF**:
  - Include model URL for direct access
  - Choose OPD range (specific diagrams or full model)
  - Quality options for printing
- **File Naming**: Default uses model name; custom names supported

### Model Templates

- **Access**: Secondary toolbar > insert template button
- **Template Types**:
  - Private: Created by current user
  - Organizational: Shared within organization (admin-created)
  - Global: Available to all OPCloud users (system admin-created)
- **Usage**:
  - Preview: Hover to see system diagram popup
  - Load: Insert into current model
  - Double-click: Alternative to load button
- **Multi-OPD Templates**: Inserted under current OPD; creates child diagrams
- **Folder Support**: Organize templates in folders similar to regular models
- **Template Updates**: Changes to source template don't automatically update inserted copies

### Organization Ontology

- **Purpose**: Enforce consistent terminology across organization
- **Enforcement Levels**:
  - None: No restrictions
  - Suggest: Popup suggests correct term (current default)
  - Enforce: Prevents non-standard terms
- **Synonym Handling**: Suggestion popup when using non-standard term
- **Replacement**: Click suggested term to replace automatically
- **Auto Format Interaction**: Disabling auto format when selecting suggested term
- **Admin Setup**: Settings > Organization Management
- **Enforcement Setting**: OPCloud Settings page > Ontology Enforcement Level

### Name Coherency

- **Duplicate Prevention**: Warning when creating object with existing name
- **Warning Dialog**: Shows where existing item is located in model
- **Options**:
  - Use existing thing: Create same logical thing with different visual instance
  - Rename: Change to unique name
  - Close: Keep default name (not recommended)
- **Visual Instance Restriction**: Cannot make different-type things visual instances of each other
- **Same-Type Requirement**: Visual instances only work for identical element types
- **In-Zoom Context**: Creating objects with same name in different OPD contexts

### Model Permissions

- **Share Options**:
  - Read permission: View-only access
  - Edit (writable) permission: Modify model
- **Group Sharing**: Select entire group or specific users
- **Organization Limitation**: Cannot share across organizations
- **Access Location**: Share button near model name
- **Owner Icon**: Key icon indicates model owner
- **Edit Token**: Pen icon shows current editor
- **Permission Hierarchy**: Must have read before write permission
- **Admin Override**: Owner or admin can modify permissions at any time

### Moving Models

- **Cut/Paste**: Use cut model and paste in destination folder
- **Versions**: Move includes auto-save and version history
- **Detailed View**: Alternative to icon view for model management
- **Workflow**:
  1. Open load menu
  2. Select model to move
  3. Use cut model
  4. Navigate to destination folder
  5. Use paste model
  6. Confirm warning dialog
- **Show Versions Toggle**: View version history alongside model
- **Auto-Save Inclusion**: Version folder moves with model

### Sub-Models

- **Purpose**: Allow concurrent work on subsystems by different modelers
- **Minimal Interconnection**: Keep main model and sub-model connections minimal
- **Creation**: Select subsystem element > create sub-model
- **Integration**: Maintain OPM methodology compatibility
- **Benefits**: Multiple team members can work simultaneously
- **First Implementation**: Initial version with planned future enhancements
- **Scope**: Subsystem-level separation; not full model branching


## Settings and Preferences

### User Settings

- **Profile**: Name, address, access level management
- **Password Reset**: Via email (not available for SSO users)
- **OPL Settings**:
  - Language: Chinese, French, German, Korean, and more (continuously expanding)
  - Thing's Default Essence: Physical (default) or Informational organizational default
  - OPL Display: Show all sentences or only non-default essence sentences
  - Units Display: Always show, hide, or only when applicable
  - Alias Display: Toggle visibility of aliases
  - Numbering: Toggle OPL numbering on/off
- **Access Methods**: Main Menu > User Settings OR gear icon near modeler name

### Model Settings

- **OPD3 Arrangement**:
  - Automatic: Tree reorders based on in-zoom process order
  - Manual: User controls exact ordering
- **Organization Defaults**:
  - Inherited from org admin settings
  - User can override in personal settings
  - Affects new models unless changed
- **Access**: Settings > OPCloud Settings


## Integration Features

### MQTT Protocol

- **Purpose**: Connect to IoT devices (Arduino, ESP8266, ESP32, etc.)
- **Configuration**: Settings > configure MQTT server (default: localhost:1883)
- **Publish/Subscribe**: Define topics for sensor data (e.g., ldr1, ldr2 topics)
- **Real-time Simulation**: Test IoT systems in OPCloud
- **Example Model**: Optimal Light Power Consumption
  - LDRs (Light Dependent Resistors): Light sensors
  - Microcontroller: Processing unit
  - Room Light: Controlled output
  - Power Calculation: Average of two sensors
  - Self-invocation: Infinite loop for continuous monitoring
- **Setup**: Configure raw server and MQTT server in preferences

### ROS Connection

- **Purpose**: Connect to Robot Operating System (ROS)
- **Requirements**: Advanced feature; requires ROS knowledge, ROS architecture understanding
- **Message Types**: Create, publish messages to ROS master
- **Subscription**: Receive messages from ROS topics
- **Example Model**: Turtle Scene (standard ROS example)
- **Workflow**:
  1. Define message creation process
  2. Publish to ROS master
  3. Monitor feedback loop
  4. Handle conditions and iteration counters
- **Integration**: Messages connect to actual robot for real-world control


## Simulation and Execution

### Conceptual Simulation

- **Access**: Main toolbar > simulation/execution button
- **Simulation Toolbar**: Multiple buttons for various options (sink simulation, stop, etc.)
- **Animation Speed**: Adjust slider (default: 1 second per operation)
- **Token Flow**: Visual representation of process execution with moving tokens
- **Validation**: Check if model behaves as expected
- **Process Order**: Tokens follow in-zoom process hierarchy (top to bottom)
- **Common Issues**: Process execution order may need adjustment (e.g., location calculation before call transmission)
- **Conceptual vs Execution**: Conceptual = visual simulation; Execution = actual calculations

### Computational Objects and Processes

- **Convert to Computational**: Select object/process > computation option
- **Value Types**: Integer, float, string, character, boolean
- **Units**: Define measurement units (meters, centimeters, seconds, etc.)
- **Alias**: Short name for use in calculations (e.g., "o1", "o2")
- **Predefined Functions**: Addition, subtraction, multiplication, division, average, custom
- **Update**: Click update or press Enter to confirm changes
- **Tooltip Display**: Visual indicator of computational nature
- **Computation Process**: Changed to show braces {} in diagram

### Advanced Calculations

- **Stereotypes**: Define parameter types (e.g., Point with X/Y coordinates)
  - Global stereotypes: Available to all users (marked with G icon)
  - Organizational stereotypes: Created by org admin (no G icon)
- **User-Defined Functions**: Custom calculations integrated via API
- **Point-Slope Example**: Two-point calculation demonstrating computational modeling
  - Define two points as objects
  - Set X and Y coordinates as computational attributes
  - Create calculation process using formula
- **API Integration**: OPCloud provides built-in functions accessible in calculations
- **Stereotype Components**: Parameters with ranges for each element

### Range Validation

- **Setup**: Select computational object > entities extension > set range
- **Value Types**: Integer, float, string, character, boolean
- **Range Definition**:
  - Start value and end value
  - Inclusion/exclusion brackets: [inclusive, (exclusive
  - Multiple ranges supported (e.g., 1-10 and 20-30)
- **Range Format Example**: [1,10][20,30] means 1-10 and 20-30 inclusive
- **State Indication**: Current state shows which range is active
- **Type Attribute**: Automatically created attribute called "type" with range options
- **Validation**: System enforces valid input ranges during simulation

### Conditions and Loops

- **Conditions**: Connect states to processes via instrument-condition links
- **Loop Creation**: Use invocation links for iteration
- **Process States**: Track iteration count and completion
- **State-Based Logic**:
  - Yes/No states for binary decisions
  - Multiple states for complex conditions
- **Visual Indicators**: Links show condition type in diagram
- **Termination**: Process completes when condition is not met

### User Input in Simulation

- **Agent Requirement**: User must be connected via agent link to process
- **Input Process**: Mark process to get user input during simulation
- **Input Object**: Create computational object to receive user values
- **Computational Integration**: Use user-defined functions with input variables
- **User Input Variable**: Pre-defined in API (available in function dropdown)
- **Effect Links**: Use to update computational objects with user-provided values
- **Workflow**:
  1. Create user as physical object
  2. Connect to process via agent link
  3. Mark process to get input
  4. Create input object (computational)
  5. Link process to input object


## Requirements Modeling

- **Purpose**: Add, remove, and view requirements on model elements
- **Access**: Select element > OPM Requirements group > Add requirements
- **Actions**:
  - Add requirements: Attach requirements to elements
  - Remove requirements: Delete requirements from elements
  - Create requirements view: Generate consolidated view of all requirements
- **Link Types for Requirements**:
  - Exhibition: Shows presence or absence
  - Characterization: Shows characteristics or attributes
  - Aggregation Participation: Shows part-whole relationships (e.g., door consists of peephole)
- **Requirements View**: Create consolidated view showing all requirements across model
- **Application**: Attach requirements to elements, links, or entire diagrams

### Requirements Example (Door-Peephole System)

- **System**: Door with peephole
- **Requirements**:
  - Peephole is part of door (aggregation participation link)
  - Typical height: 56-64 inches
  - Components: lens and sleeves (two parts)
  - Optional: peephole cover
  - Function: One-way view for seeing visitors


## Model Analysis

### System Map

- **Purpose**: Visual overview of entire model OPD tree as minimized icons
- **Creation**: Main Menu > Model Options > System Map
- **Display**: Each node minimized as icon showing connections
- **Navigation**: Click any OPD to navigate directly
- **Interconnections**: Shows in-zoom and unfold relationships
- **Large Models**: Essential for understanding complex model structure
- **Exit**: Double-click or close to return to standard view

### Model Informativeness Grading

- **Access**: Settings > Analyze Model > Model Knowledge (premium feature)
- **Classification**: OPPL sentences categorized as:
  - Definition: What things are
  - Structural: How things connect
  - Procedural: How processes work
  - Meta: Information about the model
  - Unknown: Unclassified
- **Scoring**: Weighted informative score per category
- **Metrics**:
  - Total informative level
  - Weighted informative score
  - INF average of model
  - Total OPPL sentences count
- **Purpose**: Identify missing precedence links, processes without inputs/outputs
- **Enhancement**: Compare model versions over time for improvement tracking

### Identification of Missing Knowledge

- **Access**: Settings > Analyze Model > Model Knowledge > Identification of Missing Knowledge
- **Reasoning Types**:
  - **Pistol**: Fast browser-based algorithm (quick results, may have limitations)
    - Quick online algorithm
    - Runs in browser
    - Good for initial filtering
    - May have suggestion limitations
  - **RGCN**: Python-based (better results, currently disabled)
    - Behind the scenes processing
    - More accurate suggestions
- **Confidence Threshold**: Filter suggestions by confidence level (default: 0.5 = 50%)
- **Filtering**: Adjust threshold higher for more confident suggestions only
- **Suggestions**: Objects, links, or other relations that may be missing

### AI Requirements Generation

- **Access**: Generative AI menu > AI Requirement Generation
- **Output Options**:
  - Download as Excel file
  - Copy to clipboard
- **Content Generated**:
  - Requirement text
  - Verification type
  - Acceptance criteria
  - Model triplets (source, target, link relationships)
- **Processing**:
  - Takes model OPPL as input
  - Generates requirements based on OPM specification
  - Ensures readability and guidelines compliance
- **Processing Time**: Varies with model size; larger models take longer
- **Limitations**: Auto-generated; not guaranteed to cover everything
- **Copy Workflow**: Generate > Copy to clipboard > Paste in document


## Data Import

### CSV Import for Attributes

- **Purpose**: Bulk add attribute instances and values efficiently
- **Access**: Select object > entities extension > add attribute instances and values from CSV
- **Requirements**: Object must not be an instance itself (not connected via instance structure link)
- **Options**:
  - File Selection: Browse and select CSV file
  - Ignore existing: Update existing attribute values (default: ignore)
  - Create non-existing: Add new attributes that don't exist
  - Non-computational instances: Create as non-computational with single state
  - Auto format: Toggle capitalization (default: enabled)
- **Preview**: Review before importing to verify data
- **CSV Format**: Column-based with attribute names and values


## Stereotypes

- **Purpose**: Pre-defined templates for common patterns (e.g., Security Level Computing)
- **Creation**: Admin creates stereotypes for organization
- **Usage**: Select thing > entities extension > set stereotype
- **Components**: Stereotypes can include sub-components with parameter ranges
- **Global vs Organizational**: Identified by icon (G = global, none = organizational)
- **Removal Options**:
  - Unlink: Remove stereotype but keep components in diagram
  - Unlink and remove: Remove stereotype and all added components
- **Bring Connected**: View stereotype components in other OPDs
- **Semi-Folding**: Alternative to view internal structure


## OPD3 Management

- **Access**: Secondary toolbar > OPD management button
- **Features**:
  - Search OPD by name or number (use filter)
  - Hide/show names: Toggle between numbers and full names
  - Open: Navigate to specific OPD
  - Cut: Remove OPD from current location
  - Remove: Delete OPD from model
  - Paste: Insert OPD in new location
  - Drag: Reposition OPD in tree
- **Auto-Arrangement**: Drag to reorder; affects automatic tree layout
- **Tree Navigation**: Parent-child relationships maintained


## Workflow Tips

### Bring Connected Things

- **From Secondary Toolbar**: Select element > bring connected elements
- **Link Types**:
  - Procedural links (default): Instrument, consumption, effect
  - Fundamental links: Exhibition, characterization
- **Filtered Bring**: Select specific things, then bring links between selected entities only
- **Direct Connection**: Only directly connected things brought; not parent-child relations
- **Example Workflow**:
  1. Select source element
  2. Choose link type filter
  3. Click bring to add connected elements

### Multiple Selection

- **Ctrl+Key**: Hold Ctrl and click to select multiple elements
- **Lasso Selection**: Drag rectangle to select area (all elements in range)
- **Bulk Operations**: Connect multiple elements at once
  - Select all target elements
  - Connect to single destination
  - Creates links to all selected
- **Deselection**: Click outside selection to clear

### Alignment

- **Vertexes**: Black dots on links; click to add vertex for routing
- **Vertex Addition**: Click on link line to create new routing point
- **Vertex Removal**: Drag vertex to merge back into line
- **Grid**: Use grid feature for precise alignment
- **Auto-Arrange**: System map provides automatic layout
- **Manual Adjustment**: Drag elements after auto-arrange for fine-tuning


## Summary

This tutorial series covers the complete OPCloud workflow:

1. **Fundamentals**: Create objects, processes, links, save/load
2. **Core Features**: OPD navigation, states, styles, search
3. **Advanced Modeling**: Inner/outer objects, semi-folding, in-zoom/unfold
4. **Management**: Export, templates, permissions, sub-models
5. **Requirements**: Add, remove, view requirements with aggregation links
6. **Analysis**: System map, informativeness grading, missing knowledge
7. **Integration**: MQTT, ROS connections
8. **Simulation**: Conceptual and computational, conditions, loops, user input
9. **Automation**: CSV import, AI requirements generation

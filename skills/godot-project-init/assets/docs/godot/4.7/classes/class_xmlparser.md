> Source: https://docs.godotengine.org/en/4.7/classes/class_xmlparser.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="xmlparser"></a>

<a id="class-xmlparser"></a>

# XMLParser

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Provides a low-level interface for creating parsers for XML files.

<a id="description"></a>

## Description

Provides a low-level interface for creating parsers for [XML](https://en.wikipedia.org/wiki/XML) files. This class can serve as base to make custom XML parsers.

To parse XML, you must open a file with the [open()](class_xmlparser.md#class-xmlparser-method-open) method or a buffer with the [open_buffer()](class_xmlparser.md#class-xmlparser-method-open-buffer) method. Then, the [read()](class_xmlparser.md#class-xmlparser-method-read) method must be called to parse the next nodes. Most of the methods take into consideration the currently parsed node.

Here is an example of using **XMLParser** to parse an SVG file (which is based on XML), printing each element and its attributes as a dictionary:

```gdscript
var parser = XMLParser.new()
parser.open("path/to/file.svg")
while parser.read() != ERR_FILE_EOF:
    if parser.get_node_type() == XMLParser.NODE_ELEMENT:
        var node_name = parser.get_node_name()
        var attributes_dict = {}
        for idx in range(parser.get_attribute_count()):
            attributes_dict[parser.get_attribute_name(idx)] = parser.get_attribute_value(idx)
        print("The ", node_name, " element has the following attributes: ", attributes_dict)
```

```csharp
var parser = new XmlParser();
parser.Open("path/to/file.svg");
while (parser.Read() != Error.FileEof)
{
    if (parser.GetNodeType() == XmlParser.NodeType.Element)
    {
        var nodeName = parser.GetNodeName();
        var attributesDict = new Godot.Collections.Dictionary();
        for (int idx = 0; idx < parser.GetAttributeCount(); idx++)
        {
            attributesDict[parser.GetAttributeName(idx)] = parser.GetAttributeValue(idx);
        }
        GD.Print($"The {nodeName} element has the following attributes: {attributesDict}");
    }
}
```

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [int](class_int.md#class-int) | [get_attribute_count](class_xmlparser.md#class-xmlparser-method-get-attribute-count)() const |
| [String](class_string.md#class-string) | [get_attribute_name](class_xmlparser.md#class-xmlparser-method-get-attribute-name)(idx: [int](class_int.md#class-int)) const |
| [String](class_string.md#class-string) | [get_attribute_value](class_xmlparser.md#class-xmlparser-method-get-attribute-value)(idx: [int](class_int.md#class-int)) const |
| [int](class_int.md#class-int) | [get_current_line](class_xmlparser.md#class-xmlparser-method-get-current-line)() const |
| [String](class_string.md#class-string) | [get_named_attribute_value](class_xmlparser.md#class-xmlparser-method-get-named-attribute-value)(name: [String](class_string.md#class-string)) const |
| [String](class_string.md#class-string) | [get_named_attribute_value_safe](class_xmlparser.md#class-xmlparser-method-get-named-attribute-value-safe)(name: [String](class_string.md#class-string)) const |
| [String](class_string.md#class-string) | [get_node_data](class_xmlparser.md#class-xmlparser-method-get-node-data)() const |
| [String](class_string.md#class-string) | [get_node_name](class_xmlparser.md#class-xmlparser-method-get-node-name)() const |
| [int](class_int.md#class-int) | [get_node_offset](class_xmlparser.md#class-xmlparser-method-get-node-offset)() const |
| [NodeType](class_xmlparser.md#enum-xmlparser-nodetype) | [get_node_type](class_xmlparser.md#class-xmlparser-method-get-node-type)() |
| [bool](class_bool.md#class-bool) | [has_attribute](class_xmlparser.md#class-xmlparser-method-has-attribute)(name: [String](class_string.md#class-string)) const |
| [bool](class_bool.md#class-bool) | [is_empty](class_xmlparser.md#class-xmlparser-method-is-empty)() const |
| [Error](class_@globalscope.md#enum-globalscope-error) | [open](class_xmlparser.md#class-xmlparser-method-open)(file: [String](class_string.md#class-string)) |
| [Error](class_@globalscope.md#enum-globalscope-error) | [open_buffer](class_xmlparser.md#class-xmlparser-method-open-buffer)(buffer: [PackedByteArray](class_packedbytearray.md#class-packedbytearray)) |
| [Error](class_@globalscope.md#enum-globalscope-error) | [read](class_xmlparser.md#class-xmlparser-method-read)() |
| [Error](class_@globalscope.md#enum-globalscope-error) | [seek](class_xmlparser.md#class-xmlparser-method-seek)(position: [int](class_int.md#class-int)) |
| void | [skip_section](class_xmlparser.md#class-xmlparser-method-skip-section)() |

---


<a id="enumerations"></a>

## Enumerations

<a id="enum-xmlparser-nodetype"></a>

enum **NodeType**: [🔗](class_xmlparser.md#enum-xmlparser-nodetype)

<a id="class-xmlparser-constant-node-none"></a>

[NodeType](class_xmlparser.md#enum-xmlparser-nodetype) **NODE_NONE** = `0`

There's no node (no file or buffer opened).

<a id="class-xmlparser-constant-node-element"></a>

[NodeType](class_xmlparser.md#enum-xmlparser-nodetype) **NODE_ELEMENT** = `1`

An element node type, also known as a tag, e.g. `<title>`.

<a id="class-xmlparser-constant-node-element-end"></a>

[NodeType](class_xmlparser.md#enum-xmlparser-nodetype) **NODE_ELEMENT_END** = `2`

An end of element node type, e.g. `</title>`.

<a id="class-xmlparser-constant-node-text"></a>

[NodeType](class_xmlparser.md#enum-xmlparser-nodetype) **NODE_TEXT** = `3`

A text node type, i.e. text that is not inside an element. This includes whitespace.

<a id="class-xmlparser-constant-node-comment"></a>

[NodeType](class_xmlparser.md#enum-xmlparser-nodetype) **NODE_COMMENT** = `4`

A comment node type, e.g. `<!--A comment-->`.

<a id="class-xmlparser-constant-node-cdata"></a>

[NodeType](class_xmlparser.md#enum-xmlparser-nodetype) **NODE_CDATA** = `5`

A node type for CDATA (Character Data) sections, e.g. `<![CDATA[CDATA section]]>`.

<a id="class-xmlparser-constant-node-unknown"></a>

[NodeType](class_xmlparser.md#enum-xmlparser-nodetype) **NODE_UNKNOWN** = `6`

An unknown node type.

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-xmlparser-method-get-attribute-count"></a>

[int](class_int.md#class-int) **get_attribute_count**() const [🔗](class_xmlparser.md#class-xmlparser-method-get-attribute-count)

Returns the number of attributes in the currently parsed element.

**Note:** If this method is used while the currently parsed node is not [NODE_ELEMENT](class_xmlparser.md#class-xmlparser-constant-node-element) or [NODE_ELEMENT_END](class_xmlparser.md#class-xmlparser-constant-node-element-end), this count will not be updated and will still reflect the last element.

---


<a id="class-xmlparser-method-get-attribute-name"></a>

[String](class_string.md#class-string) **get_attribute_name**(idx: [int](class_int.md#class-int)) const [🔗](class_xmlparser.md#class-xmlparser-method-get-attribute-name)

Returns the name of an attribute of the currently parsed element, specified by the `idx` index.

---


<a id="class-xmlparser-method-get-attribute-value"></a>

[String](class_string.md#class-string) **get_attribute_value**(idx: [int](class_int.md#class-int)) const [🔗](class_xmlparser.md#class-xmlparser-method-get-attribute-value)

Returns the value of an attribute of the currently parsed element, specified by the `idx` index.

---


<a id="class-xmlparser-method-get-current-line"></a>

[int](class_int.md#class-int) **get_current_line**() const [🔗](class_xmlparser.md#class-xmlparser-method-get-current-line)

Returns the current line in the parsed file, counting from 0.

---


<a id="class-xmlparser-method-get-named-attribute-value"></a>

[String](class_string.md#class-string) **get_named_attribute_value**(name: [String](class_string.md#class-string)) const [🔗](class_xmlparser.md#class-xmlparser-method-get-named-attribute-value)

Returns the value of an attribute of the currently parsed element, specified by its `name`. This method will raise an error if the element has no such attribute.

---


<a id="class-xmlparser-method-get-named-attribute-value-safe"></a>

[String](class_string.md#class-string) **get_named_attribute_value_safe**(name: [String](class_string.md#class-string)) const [🔗](class_xmlparser.md#class-xmlparser-method-get-named-attribute-value-safe)

Returns the value of an attribute of the currently parsed element, specified by its `name`. This method will return an empty string if the element has no such attribute.

---


<a id="class-xmlparser-method-get-node-data"></a>

[String](class_string.md#class-string) **get_node_data**() const [🔗](class_xmlparser.md#class-xmlparser-method-get-node-data)

Returns the contents of a text node. This method will raise an error if the current parsed node is of any other type.

---


<a id="class-xmlparser-method-get-node-name"></a>

[String](class_string.md#class-string) **get_node_name**() const [🔗](class_xmlparser.md#class-xmlparser-method-get-node-name)

Returns the name of a node. This method will raise an error if the currently parsed node is a text node.

**Note:** The content of a [NODE_CDATA](class_xmlparser.md#class-xmlparser-constant-node-cdata) node and the comment string of a [NODE_COMMENT](class_xmlparser.md#class-xmlparser-constant-node-comment) node are also considered names.

---


<a id="class-xmlparser-method-get-node-offset"></a>

[int](class_int.md#class-int) **get_node_offset**() const [🔗](class_xmlparser.md#class-xmlparser-method-get-node-offset)

Returns the byte offset of the currently parsed node since the beginning of the file or buffer. This is usually equivalent to the number of characters before the read position.

---


<a id="class-xmlparser-method-get-node-type"></a>

[NodeType](class_xmlparser.md#enum-xmlparser-nodetype) **get_node_type**() [🔗](class_xmlparser.md#class-xmlparser-method-get-node-type)

Returns the type of the current node. Compare with [NodeType](class_xmlparser.md#enum-xmlparser-nodetype) constants.

---


<a id="class-xmlparser-method-has-attribute"></a>

[bool](class_bool.md#class-bool) **has_attribute**(name: [String](class_string.md#class-string)) const [🔗](class_xmlparser.md#class-xmlparser-method-has-attribute)

Returns `true` if the currently parsed element has an attribute with the `name`.

---


<a id="class-xmlparser-method-is-empty"></a>

[bool](class_bool.md#class-bool) **is_empty**() const [🔗](class_xmlparser.md#class-xmlparser-method-is-empty)

Returns `true` if the currently parsed element is empty, e.g. `<element />`.

---


<a id="class-xmlparser-method-open"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **open**(file: [String](class_string.md#class-string)) [🔗](class_xmlparser.md#class-xmlparser-method-open)

Opens an XML `file` for parsing. This method returns an error code.

---


<a id="class-xmlparser-method-open-buffer"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **open_buffer**(buffer: [PackedByteArray](class_packedbytearray.md#class-packedbytearray)) [🔗](class_xmlparser.md#class-xmlparser-method-open-buffer)

Opens an XML raw `buffer` for parsing. This method returns an error code.

---


<a id="class-xmlparser-method-read"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **read**() [🔗](class_xmlparser.md#class-xmlparser-method-read)

Parses the next node in the file. This method returns an error code.

---


<a id="class-xmlparser-method-seek"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **seek**(position: [int](class_int.md#class-int)) [🔗](class_xmlparser.md#class-xmlparser-method-seek)

Moves the buffer cursor to a certain offset (since the beginning) and reads the next node there. This method returns an error code.

---


<a id="class-xmlparser-method-skip-section"></a>

void **skip_section**() [🔗](class_xmlparser.md#class-xmlparser-method-skip-section)

Skips the current section. If the currently parsed node contains more inner nodes, they will be ignored and the cursor will go to the closing of the current element.

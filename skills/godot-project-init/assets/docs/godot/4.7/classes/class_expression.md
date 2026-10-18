> Source: https://docs.godotengine.org/en/4.7/classes/class_expression.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="expression"></a>

<a id="class-expression"></a>

# Expression

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A class that stores an expression you can execute.

<a id="description"></a>

## Description

An expression can be made of any arithmetic operation, built-in math function call, method call of a passed instance, or built-in type construction call.

An example expression text using the built-in math functions could be `sqrt(pow(3, 2) + pow(4, 2))`.

In the following example we use a [LineEdit](class_lineedit.md#class-lineedit) node to write our expression and show the result.

```gdscript
var expression = Expression.new()

func _ready():
    $LineEdit.text_submitted.connect(self._on_text_submitted)

func _on_text_submitted(command):
    var error = expression.parse(command)
    if error != OK:
        print(expression.get_error_text())
        return
    var result = expression.execute()
    if not expression.has_execute_failed():
        $LineEdit.text = str(result)
```

```csharp
private Expression _expression = new Expression();

public override void _Ready()
{
    GetNode<LineEdit>("LineEdit").TextSubmitted += OnTextEntered;
}

private void OnTextEntered(string command)
{
    Error error = _expression.Parse(command);
    if (error != Error.Ok)
    {
        GD.Print(_expression.GetErrorText());
        return;
    }
    Variant result = _expression.Execute();
    if (!_expression.HasExecuteFailed())
    {
        GetNode<LineEdit>("LineEdit").Text = result.ToString();
    }
}
```

<a id="tutorials"></a>

## Tutorials

- [Evaluating Expressions](../tutorials/scripting/evaluating_expressions.md)

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| [Variant](class_variant.md#class-variant) | [execute](class_expression.md#class-expression-method-execute)(inputs: [Array](class_array.md#class-array) = [], base_instance: [Object](class_object.md#class-object) = null, show_error: [bool](class_bool.md#class-bool) = true, const_calls_only: [bool](class_bool.md#class-bool) = false) |
| [String](class_string.md#class-string) | [get_error_text](class_expression.md#class-expression-method-get-error-text)() const |
| [bool](class_bool.md#class-bool) | [has_execute_failed](class_expression.md#class-expression-method-has-execute-failed)() const |
| [Error](class_@globalscope.md#enum-globalscope-error) | [parse](class_expression.md#class-expression-method-parse)(expression: [String](class_string.md#class-string), input_names: [PackedStringArray](class_packedstringarray.md#class-packedstringarray) = PackedStringArray()) |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-expression-method-execute"></a>

[Variant](class_variant.md#class-variant) **execute**(inputs: [Array](class_array.md#class-array) = [], base_instance: [Object](class_object.md#class-object) = null, show_error: [bool](class_bool.md#class-bool) = true, const_calls_only: [bool](class_bool.md#class-bool) = false) [🔗](class_expression.md#class-expression-method-execute)

Executes the expression that was previously parsed by [parse()](class_expression.md#class-expression-method-parse) and returns the result. Before you use the returned object, you should check if the method failed by calling [has_execute_failed()](class_expression.md#class-expression-method-has-execute-failed).

If you defined input variables in [parse()](class_expression.md#class-expression-method-parse), you can specify their values in the inputs array, in the same order.

---


<a id="class-expression-method-get-error-text"></a>

[String](class_string.md#class-string) **get_error_text**() const [🔗](class_expression.md#class-expression-method-get-error-text)

Returns the error text if [parse()](class_expression.md#class-expression-method-parse) or [execute()](class_expression.md#class-expression-method-execute) has failed.

---


<a id="class-expression-method-has-execute-failed"></a>

[bool](class_bool.md#class-bool) **has_execute_failed**() const [🔗](class_expression.md#class-expression-method-has-execute-failed)

Returns `true` if [execute()](class_expression.md#class-expression-method-execute) has failed.

---


<a id="class-expression-method-parse"></a>

[Error](class_@globalscope.md#enum-globalscope-error) **parse**(expression: [String](class_string.md#class-string), input_names: [PackedStringArray](class_packedstringarray.md#class-packedstringarray) = PackedStringArray()) [🔗](class_expression.md#class-expression-method-parse)

Parses the expression and returns an [Error](class_@globalscope.md#enum-globalscope-error) code.

You can optionally specify names of variables that may appear in the expression with `input_names`, so that you can bind them when it gets executed.

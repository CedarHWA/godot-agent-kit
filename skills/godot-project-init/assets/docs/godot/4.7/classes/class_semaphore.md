> Source: https://docs.godotengine.org/en/4.7/classes/class_semaphore.html
> Godot documentation: 4.7; format-converted, not summarized.

<a id="semaphore"></a>

<a id="class-semaphore"></a>

# Semaphore

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A synchronization mechanism used to control access to a shared resource by [Thread](class_thread.md#class-thread)s.

<a id="description"></a>

## Description

A synchronization semaphore that can be used to synchronize multiple [Thread](class_thread.md#class-thread)s. Initialized to zero on creation. For a binary version, see [Mutex](class_mutex.md#class-mutex).

**Warning:** Semaphores must be used carefully to avoid deadlocks.

**Warning:** To guarantee that the operating system is able to perform proper cleanup (no crashes, no deadlocks), these conditions must be met:

- When a **Semaphore**'s reference count reaches zero and it is therefore destroyed, no threads must be waiting on it.
- When a [Thread](class_thread.md#class-thread)'s reference count reaches zero and it is therefore destroyed, it must not be waiting on any semaphore.

<a id="tutorials"></a>

## Tutorials

- [Using multiple threads](../tutorials/performance/using_multiple_threads.md)
- [Thread-safe APIs](../tutorials/performance/thread_safe_apis.md)

<a id="methods"></a>

## Methods

|  |  |
| --- | --- |
| void | [post](class_semaphore.md#class-semaphore-method-post)(count: [int](class_int.md#class-int) = 1) |
| [bool](class_bool.md#class-bool) | [try_wait](class_semaphore.md#class-semaphore-method-try-wait)() |
| void | [wait](class_semaphore.md#class-semaphore-method-wait)() |

---


<a id="method-descriptions"></a>

## Method Descriptions

<a id="class-semaphore-method-post"></a>

void **post**(count: [int](class_int.md#class-int) = 1) [🔗](class_semaphore.md#class-semaphore-method-post)

Lowers the **Semaphore**, allowing one thread in, or more if `count` is specified.

---


<a id="class-semaphore-method-try-wait"></a>

[bool](class_bool.md#class-bool) **try_wait**() [🔗](class_semaphore.md#class-semaphore-method-try-wait)

Like [wait()](class_semaphore.md#class-semaphore-method-wait), but won't block, so if the value is zero, fails immediately and returns `false`. If non-zero, it returns `true` to report success.

---


<a id="class-semaphore-method-wait"></a>

void **wait**() [🔗](class_semaphore.md#class-semaphore-method-wait)

Waits for the **Semaphore**, if its value is zero, blocks until non-zero.

# 📝 20 — Logging in Python

> A complete beginner-to-advanced guide to Python logging, log levels, handlers, formatters, configuration, exception logging, file logging, rotating logs, custom loggers, debugging, and production-ready logging practices.

---

## 📌 Overview

When developing a Python application, `print()` statements are useful for quick debugging.

However, professional applications need something much more powerful.

They need **logging**.

Logging allows an application to record important information about what is happening while the program runs.

For example:

```text
2026-09-15 10:30:12 | INFO     | Application started
2026-09-15 10:30:15 | INFO     | User logged in
2026-09-15 10:30:18 | WARNING  | Database response is slow
2026-09-15 10:30:22 | ERROR    | Failed to process payment
```

Logs help developers:

* Debug applications
* Diagnose errors
* Monitor systems
* Understand application behavior
* Investigate failures
* Track important events
* Analyze production problems
* Monitor performance
* Maintain software

Python provides a powerful built-in logging system through the:

```python
logging
```

module.

---

# 🎯 Learning Objectives

By the end of this chapter, you will understand:

* What logging is
* Why logging is important
* `print()` vs logging
* Python's `logging` module
* Log levels
* `DEBUG`
* `INFO`
* `WARNING`
* `ERROR`
* `CRITICAL`
* Creating log messages
* Logger objects
* Handlers
* Formatters
* Log files
* Logging configuration
* `basicConfig()`
* Custom loggers
* Exception logging
* `logger.exception()`
* Stack traces
* Multiple handlers
* Rotating log files
* Logging timestamps
* Logging from multiple modules
* Production logging practices
* Security considerations
* Structured logging concepts

---

# 1. What is Logging?

**Logging** is the process of recording events that occur while a program is running.

A log message may contain:

```text
Timestamp
Log Level
Logger Name
Message
```

Example:

```text
2026-09-15 10:30:15 | INFO | application | User logged in
```

A logging system provides a structured way to record these events.

---

# 2. Why Do We Need Logging?

Consider a production application with thousands of users.

Suppose something goes wrong.

A developer needs to answer questions such as:

```text
What happened?
When did it happen?
Which module failed?
Which operation was running?
What error occurred?
What happened immediately before the failure?
```

A collection of useful logs can answer these questions.

Without logs:

```text
Application crashed.
```

With logs:

```text
2026-09-15 14:20:01 INFO     User authenticated
2026-09-15 14:20:03 INFO     Payment request started
2026-09-15 14:20:05 WARNING  Payment provider response slow
2026-09-15 14:20:08 ERROR    Payment request failed
```

The second scenario gives developers much more information.

---

# 3. Logging vs `print()`

Beginners often use:

```python
print("Application started")
```

This is fine for simple experiments.

But professional applications should generally use logging.

### `print()`

```python
print("User logged in")
```

### Logging

```python
import logging

logging.info("User logged in")
```

Logging provides features that `print()` does not provide easily:

* Severity levels
* Timestamps
* Log files
* Multiple outputs
* Formatting
* Exception information
* Logger hierarchy
* Filtering
* Configuration
* Production control

---

# 4. Importing the Logging Module

Python includes logging in the standard library.

```python
import logging
```

No external package is required.

---

# 5. Your First Log Message

```python
import logging

logging.warning("This is a warning")
```

Output typically looks similar to:

```text
WARNING:root:This is a warning
```

Python's logging system has a default root logger.

---

# 6. Basic Logging Functions

The most commonly used functions are:

```python
logging.debug()
logging.info()
logging.warning()
logging.error()
logging.critical()
```

Example:

```python
import logging

logging.debug("Debug message")
logging.info("Information message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")
```

By default, Python's root logging configuration usually displays `WARNING` and higher severity messages.

---

# 7. Logging Levels

Python provides standard log levels.

```text
DEBUG
INFO
WARNING
ERROR
CRITICAL
```

Each level represents a different severity.

---

# 8. DEBUG

`DEBUG` is used for detailed information useful during development and troubleshooting.

```python
logging.debug("Starting database query")
```

Examples:

```text
DEBUG - Function started
DEBUG - Request parameters validated
DEBUG - Database query executed
DEBUG - Cache lookup completed
```

Use DEBUG when you need detailed diagnostic information.

---

# 9. INFO

`INFO` represents normal application activity.

```python
logging.info("Application started")
```

Examples:

```text
INFO - Server started
INFO - User logged in
INFO - File uploaded
INFO - Order created
```

INFO messages should communicate normal and meaningful application events.

---

# 10. WARNING

`WARNING` indicates something unexpected or potentially problematic, but the application can continue.

```python
logging.warning("Database response time is high")
```

Examples:

```text
WARNING - Configuration value missing
WARNING - Disk space is low
WARNING - API response is slow
WARNING - Retry attempt 2 of 3
```

A warning does not necessarily mean the application failed.

---

# 11. ERROR

`ERROR` indicates that an operation failed.

```python
logging.error("Failed to connect to database")
```

Examples:

```text
ERROR - File could not be opened
ERROR - Payment failed
ERROR - Database query failed
ERROR - API request failed
```

The application may still continue running.

---

# 12. CRITICAL

`CRITICAL` represents a severe failure that may prevent the application from continuing correctly.

```python
logging.critical("Database service is unavailable")
```

Examples:

```text
CRITICAL - Application configuration is corrupted
CRITICAL - Primary database unavailable
CRITICAL - Security subsystem failed
```

Use CRITICAL sparingly.

---

# 13. Log Level Hierarchy

The levels can be viewed approximately as:

```text
DEBUG
  ↓
INFO
  ↓
WARNING
  ↓
ERROR
  ↓
CRITICAL
```

As severity increases:

```text
DEBUG     → Detailed diagnostic information
INFO      → Normal application events
WARNING   → Potential problem
ERROR     → Operation failed
CRITICAL  → Severe system failure
```

---

# 14. Setting the Logging Level

Use `basicConfig()`.

```python
import logging

logging.basicConfig(
    level=logging.DEBUG
)

logging.debug("Debug information")
logging.info("Application started")
logging.warning("Warning message")
logging.error("Error occurred")
logging.critical("Critical failure")
```

Setting the level to `DEBUG` allows all standard levels to be considered.

---

# 15. `basicConfig()`

`basicConfig()` provides a simple way to configure the logging system.

Example:

```python
import logging

logging.basicConfig(
    level=logging.INFO
)

logging.info("Application started")
```

It is useful for:

* Small scripts
* Tutorials
* Simple applications
* Prototypes

For larger applications, more structured configuration is often preferable.

---

# 16. Logging to a File

You can send logs to a file.

```python
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

logging.info("Application started")
logging.warning("Low disk space")
logging.error("Something failed")
```

This creates:

```text
app.log
```

Example:

```text
INFO:root:Application started
WARNING:root:Low disk space
ERROR:root:Something failed
```

---

# 17. Adding a Log Format

A useful production log usually contains more context.

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logging.info("Application started")
```

Example:

```text
2026-09-15 10:30:15,123 | INFO | Application started
```

---

# 18. Important Format Fields

Python logging supports many format placeholders.

Common ones include:

| Field           | Meaning         |
| --------------- | --------------- |
| `%(asctime)s`   | Timestamp       |
| `%(levelname)s` | Log level       |
| `%(message)s`   | Log message     |
| `%(name)s`      | Logger name     |
| `%(filename)s`  | Source filename |
| `%(module)s`    | Module name     |
| `%(funcName)s`  | Function name   |
| `%(lineno)d`    | Line number     |
| `%(process)d`   | Process ID      |
| `%(thread)d`    | Thread ID       |

Example:

```python
logging.basicConfig(
    format=(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(name)s | "
        "%(message)s"
    )
)
```

---

# 19. Logging the Function Name

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format=(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(funcName)s | "
        "%(message)s"
    )
)

def login():
    logging.info("User login started")

login()
```

The function name can make debugging easier.

---

# 20. Logging Line Numbers

You can include the source line number.

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format=(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(filename)s:%(lineno)d | "
        "%(message)s"
    )
)

logging.info("Testing application")
```

This can be extremely useful when troubleshooting large applications.

---

# 21. Logging Messages with Variables

You can include values in log messages.

```python
username = "Kishor"

logging.info(
    "User %s logged in",
    username
)
```

This style is preferred over constructing strings manually in many logging scenarios.

Another example:

```python
user_id = 101

logging.info(
    "Processing user ID %s",
    user_id
)
```

---

# 22. Multiple Values

```python
username = "Kishor"
user_id = 101

logging.info(
    "User %s with ID %s logged in",
    username,
    user_id
)
```

---

# 23. Why Use Logging's Formatting?

Prefer:

```python
logging.info(
    "User %s logged in",
    username
)
```

over:

```python
logging.info(
    f"User {username} logged in"
)
```

The logging framework can defer formatting until it knows the message actually needs to be emitted.

This can be beneficial when many DEBUG messages exist but DEBUG logging is disabled.

---

# 24. Creating a Custom Logger

For larger applications, create a logger for each module.

```python
import logging

logger = logging.getLogger(__name__)
```

Then:

```python
logger.info("Application started")
logger.warning("Something unexpected happened")
logger.error("Operation failed")
```

This is generally preferred over using the root logger directly throughout a multi-module application.

---

# 25. Why `__name__`?

Suppose your file is:

```text
database.py
```

Then:

```python
logger = logging.getLogger(__name__)
```

will typically create a logger associated with:

```text
database
```

If another file is:

```text
services/payment.py
```

its logger name can reflect its module path.

This makes logs easier to trace back to their source.

---

# 26. Logger Hierarchy

Python logging uses a hierarchical naming system.

For example:

```text
application
application.database
application.api
application.api.users
application.services
```

This hierarchy allows logging configuration to be organized by module or subsystem.

Example:

```python
logger = logging.getLogger(
    "application.database"
)
```

---

# 27. Logger vs Root Logger

The root logger is the top-level logger.

For simple scripts:

```python
logging.info("Started")
```

may be sufficient.

For larger applications:

```python
logger = logging.getLogger(__name__)

logger.info("Started")
```

is more maintainable.

---

# 28. Handlers

A **handler** determines where log records are sent.

Examples:

```text
Console
File
Rotating file
Email
Custom destination
```

Common handlers include:

```python
logging.StreamHandler
logging.FileHandler
logging.handlers.RotatingFileHandler
logging.handlers.TimedRotatingFileHandler
```

---

# 29. Basic Logging Architecture

A useful mental model is:

```text
Logger
   │
   ↓
Log Record
   │
   ↓
Handler
   │
   ↓
Formatter
   │
   ↓
Output
```

More precisely, log records are created by loggers and passed through handlers, while formatters determine how those records are rendered.

---

# 30. Formatter

A formatter controls the appearance of a log message.

Example:

```python
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)
```

You can then attach it to a handler.

---

# 31. Stream Handler

A `StreamHandler` sends logs to a stream, commonly the console.

```python
import logging

logger = logging.getLogger(__name__)

handler = logging.StreamHandler()

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

handler.setFormatter(formatter)

logger.addHandler(handler)

logger.warning("Warning message")
```

---

# 32. File Handler

A `FileHandler` writes logs to a file.

```python
import logging

logger = logging.getLogger(__name__)

handler = logging.FileHandler(
    "app.log",
    encoding="utf-8"
)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

handler.setFormatter(formatter)

logger.addHandler(handler)

logger.info("Application started")
```

---

# 33. Logger Level vs Handler Level

There are two important concepts:

```text
Logger Level
      ↓
Controls which records the logger processes

Handler Level
      ↓
Controls which records a particular destination receives
```

This allows powerful configurations.

For example:

```text
DEBUG+ → file
INFO+  → console
```

---

# 34. Multiple Handlers

You can send different log levels to different destinations.

Example:

```python
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler(
    "app.log",
    encoding="utf-8"
)

console_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)
```

This allows:

```text
Console → INFO and above
File    → DEBUG and above
```

---

# 35. Avoiding Duplicate Handlers

A common mistake is adding handlers repeatedly.

For example, if a function is called multiple times and creates a new handler every time, the same log message may appear multiple times.

A robust setup should ensure handlers are configured only once.

One approach:

```python
if not logger.handlers:
    logger.addHandler(handler)
```

However, application-level logging configuration is usually best performed centrally rather than repeatedly inside business functions.

---

# 36. Exception Logging

Logging exceptions is one of the most important uses of logging.

Example:

```python
import logging

try:
    result = 10 / 0

except ZeroDivisionError:
    logging.error("Division failed")
```

This records the error but does not automatically include the traceback.

---

# 37. `logger.exception()`

Inside an exception handler, use:

```python
logger.exception()
```

when you want the exception traceback included.

Example:

```python
import logging

logger = logging.getLogger(__name__)

try:
    result = 10 / 0

except ZeroDivisionError:
    logger.exception("Division failed")
```

The resulting log includes the traceback.

This is extremely useful for debugging.

---

# 38. `exc_info=True`

Another way to include exception information is:

```python
logger.error(
    "Operation failed",
    exc_info=True
)
```

This can be useful when you want explicit control over exception information.

Inside an exception handler, `logger.exception()` is often the clearer choice.

---

# 39. Logging Exceptions with Context

```python
import logging

logger = logging.getLogger(__name__)

def process_payment(order_id):
    try:
        # Payment processing
        raise RuntimeError("Payment service unavailable")

    except Exception:
        logger.exception(
            "Payment processing failed for order %s",
            order_id
        )
```

This provides both:

```text
Context
+
Traceback
```

---

# 40. `stack_info`

Python logging can also include stack information.

```python
logger.debug(
    "Debugging call path",
    stack_info=True
)
```

This is different from exception traceback information.

Use it when you need to understand the current call stack even when an exception has not occurred.

---

# 41. Logging Exceptions Correctly

Avoid:

```python
try:
    risky_operation()
except Exception as e:
    logger.error(e)
```

This may lose valuable context and traceback information.

Prefer:

```python
try:
    risky_operation()
except Exception:
    logger.exception(
        "Risky operation failed"
    )
```

---

# 42. Logging and Exception Handling

Logging does not replace exception handling.

Bad design:

```python
try:
    operation()
except Exception:
    logger.exception("Failed")
```

and then silently continuing when the operation cannot safely continue.

Logging records what happened.

Exception handling decides what the application should do about it.

These are related but different responsibilities.

---

# 43. Rotating Log Files

A log file can grow indefinitely.

For long-running applications, this can become a problem.

Python provides:

```python
RotatingFileHandler
```

Example:

```python
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = RotatingFileHandler(
    "app.log",
    maxBytes=1_000_000,
    backupCount=3,
    encoding="utf-8"
)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

handler.setFormatter(formatter)

logger.addHandler(handler)
```

The handler rotates the log when it reaches the configured size.

---

# 44. Time-Based Log Rotation

Python also provides:

```python
TimedRotatingFileHandler
```

Example:

```python
from logging.handlers import TimedRotatingFileHandler

handler = TimedRotatingFileHandler(
    "app.log",
    when="midnight",
    backupCount=7,
    encoding="utf-8"
)
```

This can create a new log file according to a time-based schedule.

Useful for:

* Daily logs
* Weekly logs
* Long-running services
* Production applications

---

# 45. Rotating Logs Architecture

```text
Application
     ↓
Logger
     ↓
Rotating Handler
     ↓
app.log
     ↓
Rotation
     ↓
app.log.1
app.log.2
app.log.3
```

This prevents a single log file from growing forever.

---

# 46. Logging to Console and File

A common application configuration is:

```text
Console
  ↓
INFO+

File
  ↓
DEBUG+
```

This gives developers useful operational information in the console while retaining more detailed diagnostic information in the log file.

---

# 47. Configuration with `dictConfig`

For larger applications, Python supports structured configuration through:

```python
logging.config.dictConfig()
```

Example:

```python
import logging
import logging.config

config = {
    "version": 1,

    "formatters": {
        "standard": {
            "format": (
                "%(asctime)s | "
                "%(levelname)s | "
                "%(name)s | "
                "%(message)s"
            )
        }
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "standard"
        }
    },

    "root": {
        "level": "INFO",
        "handlers": ["console"]
    }
}

logging.config.dictConfig(config)
```

This approach scales better for larger projects.

---

# 48. Why Centralized Logging Configuration?

Instead of configuring every module separately:

```text
module1.py
module2.py
module3.py
module4.py
```

you can configure logging centrally:

```text
              logging_config
                    │
          ┌─────────┼─────────┐
          ↓         ↓         ↓
       module1   module2   module3
```

Each module simply creates its logger:

```python
logger = logging.getLogger(__name__)
```

---

# 49. Logging Across Multiple Modules

Example project:

```text
project/
│
├── main.py
├── database.py
├── services.py
├── api.py
└── logging_config.py
```

### `database.py`

```python
import logging

logger = logging.getLogger(__name__)

def connect():
    logger.info("Connecting to database")
```

### `services.py`

```python
import logging

logger = logging.getLogger(__name__)

def process():
    logger.info("Processing request")
```

### `main.py`

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format=(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(name)s | "
        "%(message)s"
    )
)

from database import connect
from services import process

connect()
process()
```

This produces logs that identify their source module.

---

# 50. Propagation

Loggers are hierarchical.

By default, records can propagate from child loggers to ancestor loggers.

For example:

```text
application
    │
    ├── database
    ├── api
    └── services
```

A message from:

```python
logging.getLogger(
    "application.database"
)
```

can propagate toward:

```text
application
```

and eventually the root logger.

This is useful for centralized configuration.

---

# 51. Disabling Propagation

Sometimes a child logger should not send records to its parent.

You can use:

```python
logger.propagate = False
```

This should be used deliberately because disabling propagation without understanding the handler setup can cause logs to disappear.

---

# 52. Logger Levels

You can set a logger's level:

```python
logger.setLevel(logging.DEBUG)
```

Available constants include:

```python
logging.DEBUG
logging.INFO
logging.WARNING
logging.ERROR
logging.CRITICAL
```

---

# 53. Handler Levels

Handlers can also have their own levels.

```python
handler.setLevel(logging.ERROR)
```

For example:

```text
Logger
  DEBUG
    ↓
Console Handler → INFO+
    ↓
File Handler → DEBUG+
```

This gives fine-grained control.

---

# 54. Filtering Logs

Python also supports filters.

Filters can determine whether a log record should be processed.

Example:

```python
class UserFilter(logging.Filter):

    def filter(self, record):
        return "user" in record.getMessage()
```

Then:

```python
handler.addFilter(UserFilter())
```

Filters are useful when applications need specialized logging rules.

---

# 55. Logging Context

Sometimes you need additional information such as:

```text
user_id
request_id
transaction_id
order_id
```

Example:

```python
logger.info(
    "Order processed",
    extra={
        "order_id": 12345
    }
)
```

For more advanced systems, tools such as `LoggerAdapter`, filters, or structured logging patterns can provide better context management.

---

# 56. `LoggerAdapter`

`LoggerAdapter` can attach contextual information to log records.

Conceptually:

```python
adapter = logging.LoggerAdapter(
    logger,
    {"request_id": "abc123"}
)
```

Then:

```python
adapter.info("Processing request")
```

This can help correlate events belonging to the same request.

---

# 57. Request IDs and Distributed Systems

In web applications, a request may pass through:

```text
Client
  ↓
API Gateway
  ↓
Application
  ↓
Service
  ↓
Database
```

A request ID can help connect logs from different components.

Example:

```text
request_id=abc123
```

Then:

```text
INFO request_id=abc123 Request received
INFO request_id=abc123 User authenticated
INFO request_id=abc123 Database query started
INFO request_id=abc123 Response returned
```

This makes debugging distributed systems significantly easier.

---

# 58. Structured Logging

Traditional logs often look like:

```text
2026-09-15 INFO User logged in
```

Structured logs represent fields separately.

Conceptually:

```json
{
    "timestamp": "2026-09-15T10:30:00Z",
    "level": "INFO",
    "event": "user_login",
    "user_id": 101
}
```

Structured logging is useful for:

* Log aggregation
* Search
* Monitoring
* Analytics
* Distributed systems
* Cloud environments

Python's standard `logging` module can support structured approaches, although dedicated third-party libraries are also commonly used in production systems.

---

# 59. Logging in Production

Production logging should be:

```text
Useful
Consistent
Searchable
Safe
Configurable
Performant
```

A production system should avoid excessive noise.

For example, logging every iteration of a large loop at INFO level can generate huge amounts of data.

Instead:

```python
logger.debug(
    "Processing item %s",
    item_id
)
```

can keep detailed information available when DEBUG is enabled.

---

# 60. Logging Levels in Production

A reasonable conceptual approach is:

```text
DEBUG
↓
Development diagnostics

INFO
↓
Important application events

WARNING
↓
Unexpected but recoverable situations

ERROR
↓
Failed operations

CRITICAL
↓
Severe application/system failures
```

The exact policy depends on the application.

---

# 61. What Should You Log?

Good candidates include:

```text
Application startup
Application shutdown
Authentication events
Important state changes
External service failures
Database failures
Unexpected conditions
Retries
Security-relevant events
Background task failures
```

---

# 62. What Should You NOT Log?

Never casually log sensitive information.

Avoid logging:

```text
Passwords
API keys
Authentication tokens
Credit card numbers
Private keys
Session secrets
Sensitive personal information
```

Bad:

```python
logger.info(
    "User password: %s",
    password
)
```

Good:

```python
logger.info(
    "Password authentication attempted"
)
```

---

# 63. Logging and Privacy

Logs can become a source of sensitive data leakage.

Remember:

```text
Application Data
      ↓
Logs
      ↓
Log Storage
      ↓
Backups
      ↓
Monitoring Systems
```

A value that is logged may exist in many systems.

Therefore, treat logs as sensitive operational data.

---

# 64. Logging Performance

Logging itself has a cost.

Avoid unnecessarily expensive operations when the relevant log level is disabled.

For example:

```python
if logger.isEnabledFor(logging.DEBUG):
    logger.debug(
        "Large object: %s",
        expensive_operation()
    )
```

This can prevent expensive work when DEBUG logging is disabled.

Use this optimization only when the computation is genuinely expensive.

---

# 65. Logging and `isEnabledFor()`

Example:

```python
if logger.isEnabledFor(logging.DEBUG):
    logger.debug(
        "Detailed state: %s",
        expensive_state_calculation()
    )
```

This checks whether DEBUG logging is enabled before performing the expensive calculation.

---

# 66. Logging in Exception Handling

A strong pattern is:

```python
try:
    process_data()

except ValueError:
    logger.exception(
        "Invalid data received"
    )

except ConnectionError:
    logger.exception(
        "External service unavailable"
    )
```

This provides meaningful context for different failure types.

---

# 67. Avoid Catching Everything Without Reason

Avoid:

```python
try:
    process()
except Exception:
    logger.exception("Something went wrong")
```

unless you have a clear reason for catching at that boundary.

Sometimes the correct design is to let an exception propagate to a higher-level handler.

Logging should happen where the failure can be understood and handled appropriately.

---

# 68. Logging Anti-Patterns

## ❌ Using `print()` everywhere

```python
print("Error")
```

Use logging for application diagnostics.

---

## ❌ Logging everything at ERROR

Bad:

```python
logger.error("User logged in")
```

Better:

```python
logger.info("User logged in")
```

---

## ❌ Logging sensitive information

Never log secrets.

---

## ❌ Duplicate logging

Avoid logging the same exception at multiple unrelated layers unless each layer adds meaningful context.

---

## ❌ Huge log messages

Avoid dumping enormous objects unnecessarily.

---

## ❌ Unstructured messages everywhere

Prefer consistent event messages and useful context.

---

# 69. Example — Professional Logger Setup

```python
import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler(
    "application.log",
    encoding="utf-8"
)
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s | "
    "%(levelname)s | "
    "%(name)s | "
    "%(filename)s:%(lineno)d | "
    "%(message)s"
)

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)
```

Now:

```python
logger.debug("Detailed diagnostic information")
logger.info("Application started")
logger.warning("Configuration is incomplete")
logger.error("Database query failed")
logger.critical("System cannot continue")
```

---

# 70. Example — Application Service

```python
import logging

logger = logging.getLogger(__name__)


def create_user(username, email):

    logger.info(
        "Creating user: %s",
        username
    )

    try:
        # Simulated operation
        if not email:
            raise ValueError(
                "Email is required"
            )

        logger.info(
            "User created successfully: %s",
            username
        )

    except ValueError:
        logger.exception(
            "User creation failed: %s",
            username
        )
        raise
```

Important design principle:

```text
Log
 ↓
Preserve context
 ↓
Handle or re-raise appropriately
```

---

# 71. Logging Architecture for a Larger Project

A scalable structure might look like:

```text
project/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── api.py
│   └── services.py
│
├── config/
│   └── logging_config.py
│
├── logs/
│   └── application.log
│
└── tests/
```

Each module:

```python
logger = logging.getLogger(__name__)
```

Central configuration:

```text
logging_config.py
        ↓
Application
        ↓
Modules
        ↓
Handlers
        ↓
Logs
```

---

# 72. Testing Logging

Logging can also be tested.

For example, tests may verify that:

```text
ERROR
```

is emitted when an expected failure occurs.

In Python testing environments, tools such as `pytest` provide mechanisms for capturing logs.

The key idea is:

```text
Application Behavior
        +
Expected Logging
        ↓
Test
```

---

# 73. Logging vs Monitoring

Logging and monitoring are related but different.

### Logging

Answers:

> What happened?

Example:

```text
Database connection failed.
```

### Monitoring

Answers:

> How is the system behaving?

Examples:

```text
CPU usage
Memory usage
Request rate
Error rate
Latency
Availability
```

A mature production system often uses both.

---

# 74. Logging vs Debugging

### Debugging

Usually involves actively investigating a problem.

### Logging

Creates a historical record that can help with that investigation.

Think:

```text
Logging
   ↓
Evidence

Debugging
   ↓
Investigation
```

---

# 75. Logging in Web Applications

A web application may log:

```text
Request received
Authentication
Authorization
Database operation
External API call
Response status
Request duration
Exception
```

Example:

```text
INFO | GET /users/101
INFO | User authenticated
INFO | Database query completed
INFO | Response 200
```

---

# 76. Logging API Requests

Useful fields may include:

```text
HTTP method
Path
Status code
Request ID
Duration
User ID
```

Avoid logging sensitive request bodies or authorization headers.

---

# 77. Logging Database Operations

Useful:

```python
logger.debug(
    "Executing user lookup for ID %s",
    user_id
)
```

Avoid logging:

```text
Passwords
Connection secrets
Full sensitive records
```

---

# 78. Logging Background Jobs

For scheduled tasks:

```python
logger.info("Background job started")

try:
    run_job()
    logger.info("Background job completed")

except Exception:
    logger.exception(
        "Background job failed"
    )
```

This makes scheduled systems easier to monitor.

---

# 79. Logging Retries

When retrying an operation:

```python
logger.warning(
    "Request failed. Retry %s of %s",
    attempt,
    max_attempts
)
```

This helps operators understand repeated failures.

---

# 80. Logging and Time

Always include timestamps in operational logs.

Example:

```python
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)
```

Timestamps are critical when reconstructing the sequence of events.

For distributed systems, using a consistent timezone strategy such as UTC is generally preferable.

---

# 81. Professional Logging Checklist

Before shipping an application, ask:

```text
[ ] Are log levels used correctly?
[ ] Are timestamps included?
[ ] Are errors logged with context?
[ ] Are tracebacks preserved where appropriate?
[ ] Are secrets excluded?
[ ] Are logs written somewhere useful?
[ ] Can log files rotate?
[ ] Is logging configuration centralized?
[ ] Are module loggers named properly?
[ ] Are duplicate handlers avoided?
[ ] Is log volume reasonable?
[ ] Are production logs searchable?
[ ] Are sensitive fields sanitized?
```

---

# 82. Practice Exercises

## 🟢 Beginner

### Exercise 1

Create an INFO log:

```text
Application started
```

### Exercise 2

Create one message for every logging level.

### Exercise 3

Configure logging to display timestamps.

### Exercise 4

Write logs to `app.log`.

### Exercise 5

Create a custom log format.

---

## 🟡 Intermediate

### Exercise 6

Create a custom logger using:

```python
logging.getLogger(__name__)
```

### Exercise 7

Create a console handler.

### Exercise 8

Create a file handler.

### Exercise 9

Use different levels for console and file handlers.

### Exercise 10

Log an exception with:

```python
logger.exception()
```

### Exercise 11

Create a rotating log file.

### Exercise 12

Create a logging configuration using `dictConfig()`.

---

## 🔴 Advanced

### Exercise 13

Build a multi-module application with centralized logging.

### Exercise 14

Add request IDs to logs.

### Exercise 15

Build structured JSON logs.

### Exercise 16

Create a custom logging filter.

### Exercise 17

Build a log analyzer that counts:

```text
INFO
WARNING
ERROR
CRITICAL
```

### Exercise 18

Create a production-style application logger with:

```text
Console → INFO+
File → DEBUG+
Rotating files
Timestamp
Logger name
Module name
Line number
Exception traceback
```

---

# 83. Mini Project — Production Logger

Create:

```text
logging_project/
│
├── main.py
├── logger_config.py
├── services.py
└── logs/
```

### `logger_config.py`

```python
import logging
from logging.handlers import RotatingFileHandler


def setup_logging():

    logger = logging.getLogger()

    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(name)s | "
        "%(message)s"
    )

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)

    file_handler = RotatingFileHandler(
        "logs/application.log",
        maxBytes=1_000_000,
        backupCount=3,
        encoding="utf-8"
    )

    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(console)
    logger.addHandler(file_handler)
```

### `services.py`

```python
import logging

logger = logging.getLogger(__name__)


def process_user(user_id):

    logger.info(
        "Processing user %s",
        user_id
    )

    try:
        if user_id <= 0:
            raise ValueError(
                "Invalid user ID"
            )

    except ValueError:
        logger.exception(
            "User processing failed"
        )
        raise
```

### `main.py`

```python
from logger_config import setup_logging
from services import process_user


setup_logging()

process_user(101)
```

This mini project demonstrates:

* Custom loggers
* Multiple modules
* Centralized configuration
* Console logging
* File logging
* Log rotation
* Formatting
* Exception logging

---

# 84. Interview Questions

## Beginner

1. What is logging?
2. Why is logging better than `print()`?
3. What is the Python `logging` module?
4. What are the standard logging levels?
5. What is `DEBUG`?
6. What is `INFO`?
7. What is `WARNING`?
8. What is `ERROR`?
9. What is `CRITICAL`?
10. What does `basicConfig()` do?

## Intermediate

11. What is a logger?
12. What is a handler?
13. What is a formatter?
14. What is the difference between a logger and a handler?
15. How do you log to a file?
16. How do you customize the log format?
17. What does `getLogger(__name__)` do?
18. What is `logger.exception()`?
19. What is `exc_info=True`?
20. How do you rotate log files?
21. What is `RotatingFileHandler`?
22. What is `TimedRotatingFileHandler`?

## Advanced

23. What is logger hierarchy?
24. What is propagation?
25. How can duplicate logs occur?
26. How do you configure multiple handlers?
27. What is `dictConfig()`?
28. What is `LoggerAdapter`?
29. What are logging filters?
30. How would you add request IDs to logs?
31. What is structured logging?
32. How should logs be handled in distributed systems?
33. What information should never be logged?
34. How can logging affect application performance?
35. How would you design production-grade logging?

---

# 85. Quick Revision Cheat Sheet

### Import

```python
import logging
```

### Create logger

```python
logger = logging.getLogger(__name__)
```

### Levels

```python
logger.debug("Debug")
logger.info("Info")
logger.warning("Warning")
logger.error("Error")
logger.critical("Critical")
```

### Basic configuration

```python
logging.basicConfig(
    level=logging.INFO
)
```

### File logging

```python
logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)
```

### Formatting

```python
logging.basicConfig(
    format=(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(message)s"
    )
)
```

### Exception logging

```python
try:
    operation()

except Exception:
    logger.exception(
        "Operation failed"
    )
```

### Handler

```python
handler = logging.StreamHandler()
```

### File handler

```python
handler = logging.FileHandler(
    "app.log"
)
```

### Rotating handler

```python
from logging.handlers import RotatingFileHandler
```

### Time-based rotation

```python
from logging.handlers import TimedRotatingFileHandler
```

---

# 86. Logging Mental Model

```text
                    APPLICATION
                         │
                         ↓
                      LOGGER
                         │
                  Creates LogRecord
                         │
              ┌──────────┴──────────┐
              ↓                     ↓
          Console                 File
          Handler                Handler
              │                     │
              ↓                     ↓
         Formatter              Formatter
              │                     │
              ↓                     ↓
          Terminal              app.log
```

For a larger application:

```text
                         Application
                              │
              ┌───────────────┼───────────────┐
              ↓               ↓               ↓
          database          api            services
              │               │               │
              └───────────────┼───────────────┘
                              ↓
                    Central Configuration
                              │
                    ┌─────────┴─────────┐
                    ↓                   ↓
                 Console              File
                    │                   │
                    ↓                   ↓
                  INFO+               DEBUG+
```

---

# 87. Key Concepts to Remember

```text
Logging
   ↓
Record application events

Logger
   ↓
Creates and manages log records

Handler
   ↓
Determines where records go

Formatter
   ↓
Controls how records look

Level
   ↓
Controls severity

Filter
   ↓
Controls which records are accepted

Propagation
   ↓
Allows records to move through logger hierarchy

Exception logging
   ↓
Captures useful failure context and traceback
```

---

# 88. Final Takeaways

Logging is not simply about printing messages.

A professional logging system provides:

```text
Observability
     ↓
Context
     ↓
Diagnostics
     ↓
Monitoring
     ↓
Troubleshooting
```

The most important concepts to master are:

```text
logging
logger
handler
formatter
level
filter
propagation
exception logging
file logging
log rotation
structured logging
```

The most important beginner pattern is:

```python
import logging

logger = logging.getLogger(__name__)

logger.info("Application started")
```

The most important exception pattern is:

```python
try:
    operation()

except Exception:
    logger.exception(
        "Operation failed"
    )
```

And the most important production principles are:

```text
Log useful information.
Use appropriate log levels.
Include meaningful context.
Preserve tracebacks for unexpected failures.
Never log secrets.
Avoid duplicate logs.
Rotate large log files.
Centralize configuration.
Keep production logs searchable.
```

---

# 📚 References

* [Python Logging documentation](https://docs.python.org/3/library/logging.html?utm_source=chatgpt.com)
* [Python Logging HOWTO](https://docs.python.org/3/howto/logging.html?utm_source=chatgpt.com)
* [Python Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html?utm_source=chatgpt.com)
* [Python `logging.config` documentation](https://docs.python.org/3/library/logging.config.html?utm_source=chatgpt.com)
* [Python `logging.handlers` documentation](https://docs.python.org/3/library/logging.handlers.html?utm_source=chatgpt.com)

---

# 🧭 Python Learning Roadmap

```text
17-Regular-Expressions
          ↓
18-Date-and-Time
          ↓
19-JSON
          ↓
20-Logging
          ↓
21-Next Topic
```

---

## 🚀 What's Next?

Continue your Python journey with the next topic:

**➡️ `21-Unit-Testing`**

Keep learning. Keep debugging. Keep building production-quality Python. 🐍

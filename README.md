# app_global

From [docs.python.org](https://docs.python.org/3/faq/programming.html?highlight=global#how-do-i-share-global-variables-across-modules):

"The canonical way to share information across modules within a single program is to create a special module (often called config or cfg). Just import the config module in all modules of your application; the module then becomes available as a global name. Because there is only one instance of each module, any changes made to the module object get reflected everywhere. For example:"

<br>

See /Example/app_global_test for an illustration that can be run in VSCode

<br>

Although not illustrated, it is recommended to categorize data within the app globals to keep organized and thus reduce possiblity obscure failure:
* config.C - For global constants
* config.G - For global application state like DB connections, caches etc.
* config.opts - Application options
* config.log - Application logger
* config.printCli - Common print cli handler for clean exit during initialization

<br>

As with any global data, care should be taken when using from within any multi threading applications. Use appropriate locking mechanisms as required.

<br>

Besides improving documentation, the main source `config.py` will be left as an empty source file so that is infinitely flexible
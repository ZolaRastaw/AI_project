# AI_project
project work is to collect audio data (with metadata of creation) for AI applications. 
The solution will be used to collect samples for speech recognition system development.

functionalities:
Users are able to:
- identify themselves (login)
- start recording of an expression, selected by the application
- list expressions which have recordings
- list all recordings of an expression
- listen recordings of an expression
- listen only one selected recording
- mark a recording as confusing
- mark a recording as failed

Admin users are able to:
- same as users
- enter expressions as texts
- import list of expressions as texts (csv or xls)
- update parameters of sampling
- import parameters of sampling (csv or xls)
- delete failed recordings

Application will automatically:
- identify users
- select next expression to record
- store recorded audio data with metadata
- provide an option to export all recorded data (with metadata) into a single file, ready to transfer

Data
Parameters of sampling:
- required number of samples per expression
- number of expressions to be asked (KanBan) – how many expressions could have recordings more than 0 but less than required. In other words, how often the same expression is asked.

Metadata of sampling:
- user spoke
- date/time
- length (sec)
- audio encoding (sample rate min. 8kHz mono)
- spoken expression

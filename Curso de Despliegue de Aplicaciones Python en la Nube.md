# Curso de Despliegue de Aplicaciones Python en la Nube

![badge](piezas-landing-fundamentos-python_badge.webp)

Curso de Despliegue de Aplicaciones Python en la Nube
4.9

Publicado el 19 de noviembre de 2024

Nivel Básico
23 clases
3 horas de contenido
10 horas de práctica

Aprende a Desplegar aplicaciones Python. Utiliza WSGI, ASGI, y NGINX. Configura servidores en AWS, Linode, y DigitalOcean. Asegura tus aplicaciones con certificados SSL, optimiza tus bases de datos. Y automatizar procesos con Ansible y CI/CD con GitHub Actions para un entorno productivo eficiente.

Clases del curso

## Fundamentos de Deployment y Control de Versiones

### 1 ¿Cómo Desplegar Aplicaciones Python?

    ¿Cómo Desplegar Aplicaciones Python?
    02:27 minutos

- Recursos
    ¿Cómo las aplicaciones de Python se conectan con los servidores web?

  - El cliente hace solicitud de un página Web al servidor
  - El servidor regresa el archivo que es interpretado por un el Browser
  - Python no retorna un html retorna un output o salida que debe pasar a través de un protocolo que lo convierta en html que se entrega al servidor web que luego lo envía al cliente
  - El protocolo se llama WSGI que proceso un solo proceso
  - El protocolo más moderno se llama ASGI y realiza múltiples procesos con await para proceso asíncronos.
  - Para ejecutar el proyecto se debe instalar:
      · Crear el proyecto
      · Crear el entorno virtual con ``python3 -m venv .venv``
      · Crear el archivo que ejecuta WSGI
      · Instalar gunicorn : ``pip install gunicorn``
      · Ejecutar gunicorn : ``gunicorn –workers 2 –bind 127.0.0.1:8000 wsgi_app:app``

  WSGI vs ASGI

  Para escoger en WSGI vs ASGI se deben tomar en cuenta:
      · Tipo de aplicación
      · Manejo de I/O
      · Framework a utilizar

  Si se utiliza WSGI se debe utilizar : Gunicorn o uWSGI
  Si se utiliza ASGI se debe utilizar : Uvicorn o Daphne

### 2 Introducción a WSGI y ASGI para aplicaciones Python

    Introducción a WSGI y ASGI para aplicaciones Python
    09:35 minutos

![flow](flow.webp)

- gunicorn --help
    usage: gunicorn [OPTIONS] [APP_MODULE]

    optional arguments:
    -h, --help            show this help message and exit
    -v, --version         show program's version number and exit
    -c CONFIG, --config CONFIG
                            :ref:`The Gunicorn config file<configuration_file>`.
                            [./gunicorn.conf.py]
    -b ADDRESS, --bind ADDRESS
                            The socket to bind. [['127.0.0.1:8000']]
    --backlog INT         The maximum number of pending connections. [2048]
    -w INT, --workers INT
                            The number of worker processes for handling requests.
                            [1]
    -k STRING, --worker-class STRING
                            The type of workers to use. [sync]
    --threads INT         The number of worker threads for handling requests.
                            [1]
    --worker-connections INT
                            The maximum number of simultaneous clients. [1000]
    --max-requests INT    The maximum number of requests a worker will process
                            before restarting. [0]
    --max-requests-jitter INT
                            The maximum jitter to add to the *max_requests*
                            setting. [0]
    -t INT, --timeout INT
                            Workers silent for more than this many seconds are
                            killed and restarted. [30]
    --graceful-timeout INT
                            Timeout for graceful workers restart. [30]
    --keep-alive INT      The number of seconds to wait for requests on a Keep-
                            Alive connection. [2]
    --limit-request-line INT
                            The maximum size of HTTP request line in bytes. [4094]
    --limit-request-fields INT
                            Limit the number of HTTP headers fields in a request.
                            [100]
    --limit-request-field_size INT
                            Limit the allowed size of an HTTP request header
                            field. [8190]
    --reload              Restart workers when code changes. [False]
    --reload-engine STRING
                            The implementation that should be used to power
                            :ref:`reload`. [auto]
    --reload-extra-file FILES
                            Extends :ref:`reload` option to also watch and reload
                            on additional files [[]]
    --spew                Install a trace function that spews every line
                            executed by the server. [False]
    --check-config        Check the configuration and exit. The exit status is 0
                            if the [False]
    --print-config        Print the configuration settings as fully resolved.
                            Implies :ref:`check-config`. [False]
    --preload             Load application code before the worker processes are
                            forked. [False]
    --no-sendfile         Disables the use of ``sendfile()``. [None]
    --reuse-port          Set the ``SO_REUSEPORT`` flag on the listening socket.
                            [False]
    --chdir CHDIR         Change directory to specified directory before loading
                            apps. [/Volumes/2nSSD/018_PLATZI/Curso de Despliegue
                            de Aplicaciones Python en la Nube]
    -D, --daemon          Daemonize the Gunicorn process. [False]
    -e ENV, --env ENV     Set environment variables in the execution
                            environment. [[]]
    -p FILE, --pid FILE   A filename to use for the PID file. [None]
    --worker-tmp-dir DIR  A directory to use for the worker heartbeat temporary
                            file. [None]
    -u USER, --user USER  Switch worker processes to run as this user. [501]
    -g GROUP, --group GROUP
                            Switch worker process to run as this group. [20]
    -m INT, --umask INT   A bit mask for the file mode on files written by
                            Gunicorn. [0]
    --initgroups          If true, set the worker process's group access list
                            with all of the [False]
    --forwarded-allow-ips STRING
                            Front-end's IPs from which allowed to handle set
                            secure headers. [127.0.0.1,::1]
    --access-logfile FILE
                            The Access log file to write to. [None]
    --disable-redirect-access-to-syslog
                            Disable redirect access logs to syslog. [False]
    --access-logformat STRING
                            The access log format. [%(h)s %(l)s %(u)s %(t)s
                            "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"]
    --error-logfile FILE, --log-file FILE
                            The Error log file to write to. [-]
    --log-level LEVEL     The granularity of Error log outputs. [info]
    --capture-output      Redirect stdout/stderr to specified file in
                            :ref:`errorlog`. [False]
    --logger-class STRING
                            The logger you want to use to log events in Gunicorn.
                            [gunicorn.glogging.Logger]
    --log-config FILE     The log config file to use. [None]
    --log-config-json FILE
                            The log config to read config from a JSON file [None]
    --log-syslog-to SYSLOG_ADDR
                            Address to send syslog messages.
                            [unix:///var/run/syslog]
    --log-syslog          Send *Gunicorn* logs to syslog. [False]
    --log-syslog-prefix SYSLOG_PREFIX
                            Makes Gunicorn use the parameter as program-name in
                            the syslog entries. [None]
    --log-syslog-facility SYSLOG_FACILITY
                            Syslog facility name [user]
    -R, --enable-stdio-inheritance
                            Enable stdio inheritance. [False]
    --statsd-host STATSD_ADDR
                            The address of the StatsD server to log to. [None]
    --dogstatsd-tags DOGSTATSD_TAGS
                            A comma-delimited list of datadog statsd (dogstatsd)
                            tags to append to []
    --statsd-prefix STATSD_PREFIX
                            Prefix to use when emitting statsd metrics (a trailing
                            ``.`` is added, []
    -n STRING, --name STRING
                            A base to use with setproctitle for process naming.
                            [None]
    --pythonpath STRING   A comma-separated list of directories to add to the
                            Python path. [None]
    --paste STRING, --paster STRING
                            Load a PasteDeploy config file. The argument may
                            contain a ``#`` [None]
    --proxy-protocol      Enable detect PROXY protocol (PROXY mode). [False]
    --proxy-allow-from PROXY_ALLOW_IPS
                            Front-end's IPs from which allowed accept proxy
                            requests (comma separated). [127.0.0.1,::1]
    --keyfile FILE        SSL key file [None]
    --certfile FILE       SSL certificate file [None]
    --ssl-version SSL_VERSION
                            SSL version to use (see stdlib ssl module's).
                            [_SSLMethod.PROTOCOL_TLS]
    --cert-reqs CERT_REQS
                            Whether client certificate is required (see stdlib ssl
                            module's) [VerifyMode.CERT_NONE]
    --ca-certs FILE       CA certificates file [None]
    --suppress-ragged-eofs
                            Suppress ragged EOFs (see stdlib ssl module's) [True]
    --do-handshake-on-connect
                            Whether to perform SSL handshake on socket connect
                            (see stdlib ssl module's) [False]
    --ciphers CIPHERS     SSL Cipher suite to use, in the format of an OpenSSL
                            cipher list. [None]
    --paste-global CONF   Set a PasteDeploy global config variable in
                            ``key=value`` form. [[]]
    --permit-obsolete-folding
                            Permit requests employing obsolete HTTP line folding
                            mechanism [False]
    --strip-header-spaces
                            Strip spaces present between the header name and the
                            the ``:``. [False]
    --permit-unconventional-http-method
                            Permit HTTP methods not matching conventions, such as
                            IANA registration guidelines [False]
    --permit-unconventional-http-version
                            Permit HTTP version not matching conventions of 2023
                            [False]
    --casefold-http-method
                            Transform received HTTP methods to uppercase [False]
    --forwarder-headers FORWARDER_HEADERS
                            A list containing upper-case header field names that
                            the front-end proxy [SCRIPT_NAME,PATH_INFO]
    --header-map HEADER_MAP
                            Configure how header field names are mapped into
                            environ [drop]

- uvicorn --help
    Usage: uvicorn [OPTIONS] APP

    Options:
    --host TEXT                     Bind socket to this host.  [default:
                                    127.0.0.1]
    --port INTEGER                  Bind socket to this port.  [default: 8000]
    --uds TEXT                      Bind to a UNIX domain socket.
    --fd INTEGER                    Bind to socket from this file descriptor.
    --reload                        Enable auto-reload.
    --reload-dir PATH               Set reload directories explicitly, instead
                                    of using the current working directory.
    --reload-include TEXT           Set glob patterns to include while watching
                                    for files. Includes '*.py' by default; these
                                    defaults can be overridden with `--reload-
                                    exclude`. This option has no effect unless
                                    watchfiles is installed.
    --reload-exclude TEXT           Set glob patterns to exclude while watching
                                    for files. Includes '.*, .py[cod], .sw.*,
                                    ~*' by default; these defaults can be
                                    overridden with `--reload-include`. This
                                    option has no effect unless watchfiles is
                                    installed.
    --reload-delay FLOAT            Delay between previous and next check if
                                    application needs to be. Defaults to 0.25s.
                                    [default: 0.25]
    --workers INTEGER               Number of worker processes. Defaults to the
                                    $WEB_CONCURRENCY environment variable if
                                    available, or 1. Not valid with --reload.
    --loop [auto|asyncio|uvloop]    Event loop implementation.  [default: auto]
    --http [auto|h11|httptools]     HTTP protocol implementation.  [default:
                                    auto]
    --ws [auto|none|websockets|wsproto]
                                    WebSocket protocol implementation.
                                    [default: auto]
    --ws-max-size INTEGER           WebSocket max size message in bytes
                                    [default: 16777216]
    --ws-ping-interval FLOAT        WebSocket ping interval  [default: 20.0]
    --ws-ping-timeout FLOAT         WebSocket ping timeout  [default: 20.0]
    --ws-per-message-deflate BOOLEAN
                                    WebSocket per-message-deflate compression
                                    [default: True]
    --lifespan [auto|on|off]        Lifespan implementation.  [default: auto]
    --interface [auto|asgi3|asgi2|wsgi]
                                    Select ASGI3, ASGI2, or WSGI as the
                                    application interface.  [default: auto]
    --env-file PATH                 Environment configuration file.
    --log-config PATH               Logging configuration file. Supported
                                    formats: .ini, .json, .yaml.
    --log-level [critical|error|warning|info|debug|trace]
                                    Log level. [default: info]
    --access-log / --no-access-log  Enable/Disable access log.
    --use-colors / --no-use-colors  Enable/Disable colorized logging.
    --proxy-headers / --no-proxy-headers
                                    Enable/Disable X-Forwarded-Proto,
                                    X-Forwarded-For, X-Forwarded-Port to
                                    populate remote address info.
    --server-header / --no-server-header
                                    Enable/Disable default Server header.
    --date-header / --no-date-header
                                    Enable/Disable default Date header.
    --forwarded-allow-ips TEXT      Comma separated list of IPs to trust with
                                    proxy headers. Defaults to the
                                    $FORWARDED_ALLOW_IPS environment variable if
                                    available, or '127.0.0.1'.
    --root-path TEXT                Set the ASGI 'root_path' for applications
                                    submounted below a given URL path.
    --limit-concurrency INTEGER     Maximum number of concurrent connections or
                                    tasks to allow, before issuing HTTP 503
                                    responses.
    --backlog INTEGER               Maximum number of connections to hold in
                                    backlog
    --limit-max-requests INTEGER    Maximum number of requests to service before
                                    terminating the process.
    --timeout-keep-alive INTEGER    Close Keep-Alive connections if no new data
                                    is received within this timeout.  [default:
                                    5]
    --timeout-graceful-shutdown INTEGER
                                    Maximum number of seconds to wait for
                                    graceful shutdown.
    --ssl-keyfile TEXT              SSL key file
    --ssl-certfile TEXT             SSL certificate file
    --ssl-keyfile-password TEXT     SSL keyfile password
    --ssl-version INTEGER           SSL version to use (see stdlib ssl module's)
                                    [default: 17]
    --ssl-cert-reqs INTEGER         Whether client certificate is required (see
                                    stdlib ssl module's)  [default: 0]
    --ssl-ca-certs TEXT             CA certificates file
    --ssl-ciphers TEXT              Ciphers to use (see stdlib ssl module's)
                                    [default: TLSv1]
    --header TEXT                   Specify custom default HTTP response headers
                                    as a Name:Value pair
    --version                       Display the uvicorn version and exit.
    --app-dir TEXT                  Look for APP in the specified directory, by
                                    adding this to the PYTHONPATH. Defaults to
                                    the current working directory.
    --h11-max-incomplete-event-size INTEGER
                                    For h11, the maximum number of bytes to
                                    buffer of an incomplete event.
    --factory                       Treat APP as an application factory, i.e. a
                                    () -> <ASGI app> callable.
    --help                          Show this message and exit.

### 3 Control de versiones en Git y prácticas de versionamiento en Python

    Control de versiones en Git y prácticas de versionamiento en Python
    06:28 minutos

- Utilizamos Git para manejar las versiones del código.

    **Semantic Version**

    MAYOR.MINOR.PATCH
    1.3.5

    Significa que es”
    MAYOR: 1 --> Se debe modificar cuando se cambio mucho lo que ya hay hecho o se agregan nuevas capacidades.
    MINOR: 3 --> Se debe modificar cuando se han hechos cambio para mejorar o para aumentar la capacidad del código existente.
    PATCH: 5 --> Se debe modificar cuando se detecta un error en el código de producción y es necesario corregirlo sin esperar una versión MINOR.

    Para manejas las versiones en Git se utiliza el comando ``git tag -a v1.3.5 -m “Versión corregida”``
    · -a: significa agregar o añadir
    · -m: significa que vamos a enviar un mensaje de la versión

    ``git push origin v1.3.5``

    **Cambios en el código**

    Para manejar los cambio separados de la rama main se necesita crear ramas (``git branch [nombre de la rama]``).

    Para manejar las ramas de forma ordenada se utilizar ``git flow`` se crean cuatro ramas:
    · main --> es la rama a la que se agregan los tags de las versiones
    · develop --> es la rama a la que se le agrega el código de los programadores
    · feature --> como login
    · hotfix --> Reparación de errores o bugs

### 4 Configuración de entornos de desarrollo para despliegue

    Configuración de entornos de desarrollo para despliegue
    07:21 minutos

- Comandos utiles de la terminal:
  - ls (lista el contenido del directorio actual)
  - pwd (nos indica el directorio actual)
  - ssh (permite conectar con un servidor remoto y trabajar en el)
        usage: ssh [-46AaCfGgKkMNnqsTtVvXxYy] [-B bind_interface]
                [-b bind_address] [-c cipher_spec] [-D [bind_address:]port]
                [-E log_file] [-e escape_char] [-F configfile] [-I pkcs11]
                [-i identity_file] [-J [user@]host[:port]] [-L address]
                [-l login_name] [-m mac_spec] [-O ctl_cmd] [-o option] [-p port]
                [-Q query_option] [-R address] [-S ctl_path] [-W host:port]
                [-w local_tun[:remote_tun]] destination [command]
  - git
        uso: git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
                [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
                [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
                [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
                [--config-env=<name>=<envvar>] <command> [<args>]

        Estos son comandos comunes de Git usados en varias situaciones:

        comenzar un área de trabajo (mira también: git help tutorial)
        clone     Clonar un repositorio dentro de un nuevo directorio
        init      Crear un repositorio de Git vacío o reinicia el que ya existe

        trabajar en los cambios actuales (mira también: git help everyday)
        add       Agregar contenido de archivos al índice
        mv        Mover o cambiar el nombre a archivos, directorios o enlaces simbólicos
        restore   Restaurar archivos del árbol de trabajo
        rm        Borrar archivos del árbol de trabajo y del índice

        examinar el historial y el estado (mira también: git help revisions)
        bisect    Usar la búsqueda binaria para encontrar el commit que introdujo el bug
        diff      Mostrar los cambios entre commits, commit y árbol de trabajo, etc
        grep      Imprimir las líneas que concuerden con el patrón
        log       Mostrar los logs de los commits
        show      Mostrar varios tipos de objetos
        status    Mostrar el estado del árbol de trabajo

        crecer, marcar y ajustar tu historial común
        branch    Listar, crear, o borrar ramas
        commit    Grabar los cambios al repositorio
        merge     Juntar dos o más historiales de desarrollo juntos
        rebase    Volver a aplicar commits en la punta de otra rama
        reset     Reiniciar el HEAD actual a un estado específico
        switch    Cambiar de branch
        tag       Crear, listar, borrar o verificar un objeto de tag firmado con GPG

        colaborar (mira también: git help workflows)
        fetch     Descargar objetos y referencias de otro repositorio
        pull      Realizar un fetch e integra con otro repositorio o rama local
        push      Actualizar referencias remotas junto con sus objetos asociados

        'git help -a' y 'git help -g' listan los subcomandos disponibles y algunas
        guías de concepto. Consulta 'git help <command>' o 'git help <concepto>'
        para leer sobre un subcomando o concepto específico.
        Mira 'git help git' para una vista general del sistema.

  - curl
        Usage: curl [options...] <url>
        Options: (H) means HTTP/HTTPS only, (F) means FTP only
            --anyauth       Pick "any" authentication method (H)
        -a, --append        Append to target file when uploading (F/SFTP)
            --basic         Use HTTP Basic Authentication (H)
            --cacert FILE   CA certificate to verify peer against (SSL)
            --capath DIR    CA directory to verify peer against (SSL)
        -E, --cert CERT[:PASSWD]  Client certificate file and password (SSL)
            --cert-status   Verify the status of the server certificate (SSL)
            --cert-type TYPE  Certificate file type (DER/PEM/ENG) (SSL)
            --ciphers LIST  SSL ciphers to use (SSL)
            --compressed    Request compressed response (using deflate or gzip)
        -K, --config FILE   Read config from FILE
            --connect-timeout SECONDS  Maximum time allowed for connection
            --connect-to HOST1:PORT1:HOST2:PORT2 Connect to host (network level)
        -C, --continue-at OFFSET  Resumed transfer OFFSET
        -b, --cookie STRING/FILE  Read cookies from STRING/FILE (H)
        -c, --cookie-jar FILE  Write cookies to FILE after operation (H)
            --create-dirs   Create necessary local directory hierarchy
            --crlf          Convert LF to CRLF in upload
            --crlfile FILE  Get a CRL list in PEM format from the given file
        -d, --data DATA     HTTP POST data (H)
            --data-raw DATA  HTTP POST data, '@' allowed (H)
            --data-ascii DATA  HTTP POST ASCII data (H)
            --data-binary DATA  HTTP POST binary data (H)
            --data-urlencode DATA  HTTP POST data url encoded (H)
            --delegation STRING  GSS-API delegation permission
            --digest        Use HTTP Digest Authentication (H)
            --disable-eprt  Inhibit using EPRT or LPRT (F)
            --disable-epsv  Inhibit using EPSV (F)
            --dns-servers   DNS server addrs to use: 1.1.1.1;2.2.2.2
            --dns-interface  Interface to use for DNS requests
            --dns-ipv4-addr  IPv4 address to use for DNS requests, dot notation
            --dns-ipv6-addr  IPv6 address to use for DNS requests, dot notation
        -D, --dump-header FILE  Write the received headers to FILE
            --egd-file FILE  EGD socket path for random data (SSL)
            --engine ENGINE  Crypto engine (use "--engine list" for list) (SSL)
            --expect100-timeout SECONDS How long to wait for 100-continue (H)
        -f, --fail          Fail silently (no output at all) on HTTP errors (H)
            --fail-early    Fail on first transfer error, do not continue
            --false-start   Enable TLS False Start.
        -F, --form CONTENT  Specify HTTP multipart POST data (H)
            --form-string STRING  Specify HTTP multipart POST data (H)
            --ftp-account DATA  Account data string (F)
            --ftp-alternative-to-user COMMAND  String to replace "USER [name]" (F)
            --ftp-create-dirs  Create the remote dirs if not present (F)
            --ftp-method [MULTICWD/NOCWD/SINGLECWD]  Control CWD usage (F)
            --ftp-pasv      Use PASV/EPSV instead of PORT (F)
        -P, --ftp-port ADR  Use PORT with given address instead of PASV (F)
            --ftp-skip-pasv-ip  Skip the IP address for PASV (F)
            --ftp-pret      Send PRET before PASV (for drftpd) (F)
            --ftp-ssl-ccc   Send CCC after authenticating (F)
            --ftp-ssl-ccc-mode ACTIVE/PASSIVE  Set CCC mode (F)
            --ftp-ssl-control  Require SSL/TLS for FTP login, clear for transfer (F)
        -G, --get           Send the -d data with a HTTP GET (H)
        -g, --globoff       Disable URL sequences and ranges using {} and []
        -H, --header LINE   Pass custom header LINE to server (H)
        -I, --head          Show document info only
        -h, --help          This help text
            --hostpubmd5 MD5  Hex-encoded MD5 string of the host public key. (SSH)
        -0, --http1.0       Use HTTP 1.0 (H)
            --http1.1       Use HTTP 1.1 (H)
            --http2         Use HTTP 2 (H)
            --http2-prior-knowledge  Use HTTP 2 without HTTP/1.1 Upgrade (H)
            --ignore-content-length  Ignore the HTTP Content-Length header
        -i, --include       Include protocol headers in the output (H/F)
        -k, --insecure      Allow connections to SSL sites without certs (H)
            --interface INTERFACE  Use network INTERFACE (or address)
        -4, --ipv4          Resolve name to IPv4 address
        -6, --ipv6          Resolve name to IPv6 address
        -j, --junk-session-cookies  Ignore session cookies read from file (H)
            --keepalive-time SECONDS  Wait SECONDS between keepalive probes
            --key KEY       Private key file name (SSL/SSH)
            --key-type TYPE  Private key file type (DER/PEM/ENG) (SSL)
            --krb LEVEL     Enable Kerberos with security LEVEL (F)
            --libcurl FILE  Dump libcurl equivalent code of this command line
            --limit-rate RATE  Limit transfer speed to RATE
        -l, --list-only     List only mode (F/POP3)
            --local-port RANGE  Force use of RANGE for local port numbers
        -L, --location      Follow redirects (H)
            --location-trusted  Like '--location', and send auth to other hosts (H)
            --login-options OPTIONS  Server login options (IMAP, POP3, SMTP)
        -M, --manual        Display the full manual
            --mail-from FROM  Mail from this address (SMTP)
            --mail-rcpt TO  Mail to this/these addresses (SMTP)
            --mail-auth AUTH  Originator address of the original email (SMTP)
            --max-filesize BYTES  Maximum file size to download (H/F)
            --max-redirs NUM  Maximum number of redirects allowed (H)
        -m, --max-time SECONDS  Maximum time allowed for the transfer
            --metalink      Process given URLs as metalink XML file
            --negotiate     Use HTTP Negotiate (SPNEGO) authentication (H)
        -n, --netrc         Must read .netrc for user name and password
            --netrc-optional  Use either .netrc or URL; overrides -n
            --netrc-file FILE  Specify FILE for netrc
        -:, --next          Allows the following URL to use a separate set of options
            --no-alpn       Disable the ALPN TLS extension (H)
        -N, --no-buffer     Disable buffering of the output stream
            --no-keepalive  Disable keepalive use on the connection
            --no-npn        Disable the NPN TLS extension (H)
            --no-sessionid  Disable SSL session-ID reusing (SSL)
            --noproxy       List of hosts which do not use proxy
            --ntlm          Use HTTP NTLM authentication (H)
            --ntlm-wb       Use HTTP NTLM authentication with winbind (H)
            --oauth2-bearer TOKEN  OAuth 2 Bearer Token (IMAP, POP3, SMTP)
        -o, --output FILE   Write to FILE instead of stdout
            --pass PASS     Pass phrase for the private key (SSL/SSH)
            --path-as-is    Do not squash .. sequences in URL path
            --pinnedpubkey FILE/HASHES Public key to verify peer against (SSL)
            --post301       Do not switch to GET after following a 301 redirect (H)
            --post302       Do not switch to GET after following a 302 redirect (H)
            --post303       Do not switch to GET after following a 303 redirect (H)
            --preproxy [PROTOCOL://]HOST[:PORT] Proxy before HTTP(S) proxy
        -#, --progress-bar  Display transfer progress as a progress bar
            --proto PROTOCOLS  Enable/disable PROTOCOLS
            --proto-default PROTOCOL  Use PROTOCOL for any URL missing a scheme
            --proto-redir PROTOCOLS   Enable/disable PROTOCOLS on redirect
        -x, --proxy [PROTOCOL://]HOST[:PORT]  Use proxy on given port
            --proxy-anyauth  Pick "any" proxy authentication method (H)
            --proxy-basic   Use Basic authentication on the proxy (H)
            --proxy-digest  Use Digest authentication on the proxy (H)
            --proxy-cacert FILE CA certificate to verify peer against for proxy (SSL)
            --proxy-capath DIR CA directory to verify peer against for proxy (SSL)
            --proxy-cert CERT[:PASSWD] Client certificate file and password for proxy (SSL)
            --proxy-cert-type TYPE Certificate file type (DER/PEM/ENG) for proxy (SSL)
            --proxy-ciphers LIST SSL ciphers to use for proxy (SSL)
            --proxy-crlfile FILE Get a CRL list in PEM format from the given file for proxy
            --proxy-insecure Allow connections to SSL sites without certs for proxy (H)
            --proxy-key KEY Private key file name for proxy (SSL)
            --proxy-key-type TYPE Private key file type for proxy (DER/PEM/ENG) (SSL)
            --proxy-negotiate  Use HTTP Negotiate (SPNEGO) authentication on the proxy (H)
            --proxy-ntlm    Use NTLM authentication on the proxy (H)
            --proxy-header LINE Pass custom header LINE to proxy (H)
            --proxy-pass PASS Pass phrase for the private key for proxy (SSL)
            --proxy-ssl-allow-beast Allow security flaw to improve interop for proxy (SSL)
            --proxy-tlsv1   Use TLSv1 for proxy (SSL)
            --proxy-tlsuser USER TLS username for proxy
            --proxy-tlspassword STRING TLS password for proxy
            --proxy-tlsauthtype STRING TLS authentication type for proxy (default SRP)
            --proxy-service-name NAME  SPNEGO proxy service name
            --service-name NAME  SPNEGO service name
        -U, --proxy-user USER[:PASSWORD]  Proxy user and password
            --proxy1.0 HOST[:PORT]  Use HTTP/1.0 proxy on given port
        -p, --proxytunnel   Operate through a HTTP proxy tunnel (using CONNECT)
            --pubkey KEY    Public key file name (SSH)
        -Q, --quote CMD     Send command(s) to server before transfer (F/SFTP)
            --random-file FILE  File for reading random data from (SSL)
        -r, --range RANGE   Retrieve only the bytes within RANGE
            --raw           Do HTTP "raw"; no transfer decoding (H)
        -e, --referer       Referer URL (H)
        -J, --remote-header-name  Use the header-provided filename (H)
        -O, --remote-name   Write output to a file named as the remote file
            --remote-name-all  Use the remote file name for all URLs
        -R, --remote-time   Set the remote file's time on the local output
        -X, --request COMMAND  Specify request command to use
            --resolve HOST:PORT:ADDRESS  Force resolve of HOST:PORT to ADDRESS
            --retry NUM   Retry request NUM times if transient problems occur
            --retry-connrefused  Retry on connection refused (use with --retry)
            --retry-delay SECONDS  Wait SECONDS between retries
            --retry-max-time SECONDS  Retry only within this period
            --sasl-ir       Enable initial response in SASL authentication
        -S, --show-error    Show error. With -s, make curl show errors when they occur
        -s, --silent        Silent mode (don't output anything)
            --socks4 HOST[:PORT]  SOCKS4 proxy on given host + port
            --socks4a HOST[:PORT]  SOCKS4a proxy on given host + port
            --socks5 HOST[:PORT]  SOCKS5 proxy on given host + port
            --socks5-hostname HOST[:PORT]  SOCKS5 proxy, pass host name to proxy
            --socks5-gssapi-service NAME  SOCKS5 proxy service name for GSS-API
            --socks5-gssapi-nec  Compatibility with NEC SOCKS5 server
        -Y, --speed-limit RATE  Stop transfers below RATE for 'speed-time' secs
        -y, --speed-time SECONDS  Trigger 'speed-limit' abort after SECONDS (default: 30)
            --ssl           Try SSL/TLS (FTP, IMAP, POP3, SMTP)
            --ssl-reqd      Require SSL/TLS (FTP, IMAP, POP3, SMTP)
        -2, --sslv2         Use SSLv2 (SSL)
        -3, --sslv3         Use SSLv3 (SSL)
            --ssl-allow-beast  Allow security flaw to improve interop (SSL)
            --ssl-no-revoke    Disable cert revocation checks (WinSSL)
            --stderr FILE   Where to redirect stderr (use "-" for stdout)
            --tcp-nodelay   Use the TCP_NODELAY option
            --tcp-fastopen  Use TCP Fast Open
        -t, --telnet-option OPT=VAL  Set telnet option
            --tftp-blksize VALUE  Set TFTP BLKSIZE option (must be >512)
            --tftp-no-options  Do not send TFTP options requests
        -z, --time-cond TIME   Transfer based on a time condition
        -1, --tlsv1         Use >= TLSv1 (SSL)
            --tlsv1.0       Use TLSv1.0 (SSL)
            --tlsv1.1       Use TLSv1.1 (SSL)
            --tlsv1.2       Use TLSv1.2 (SSL)
            --tlsv1.3       Use TLSv1.3 (SSL)
            --trace FILE    Write a debug trace to FILE
            --trace-ascii FILE  Like --trace, but without hex output
            --trace-time    Add time stamps to trace/verbose output
            --tr-encoding   Request compressed transfer encoding (H)
        -T, --upload-file FILE  Transfer FILE to destination
            --url URL       URL to work with
        -B, --use-ascii     Use ASCII/text transfer
        -u, --user USER[:PASSWORD]  Server user and password
            --tlsuser USER  TLS username
            --tlspassword STRING  TLS password
            --tlsauthtype STRING  TLS authentication type (default: SRP)
            --unix-socket FILE    Connect through this Unix domain socket
        -A, --user-agent STRING  Send User-Agent STRING to server (H)
        -v, --verbose       Make the operation more talkative
        -V, --version       Show version number and quit
        -w, --write-out FORMAT  Use output FORMAT after completion
            --xattr         Store metadata in extended file attributes
        -q, --disable       Disable .curlrc (must be first parameter)

  - dig
  - traceroute
  - vim
    - editor de codigo
      - i : insert
      - esc : salir de insert
      - : comando
      - :wq (write and quit)
      - / (buscar)
      - n (next)
  - cat

Comandos útiles en los servidores linux:
· cd: para cambiar de directorio (carpeta)
· ls: para listar el contenido de un directorio (carpeta)
· pwd: para conocer la posición del directorio (carpeta) actual en el sistema de archivo (fs: file system)

Se requiere el uso de los comandos:
· ssh: para la creación de llaves para el acceso seguro al(os) servidor(es)
· git: para el control de las versiones del código
· curl: para hacer requests a una url y obtener información del servidor del sitio
· dig: permite obtener información del dominio y su ip
· traceroute: permite obtener información de los saltos que deben realizar los paquetes desde la computadora local hasta el servidor de dominio del dominio indicado
· vim o nano: editor de texto de Linux y otros sistemas operativos

### 5 Buenas prácticas en el uso de variables de entorno

    Buenas prácticas en el uso de variables de entorno
    05:52 minutos

- Variables de entorno
  - Crear variable de entorno (desde la terminal):
    - ``export VAR="value"`` por ejemplo ``export APP_MODE="local"``
    - Todas las variables de entorno son de tipo string
  - Usar una variable de entorno (desde programa python):
    - ``import os``
    - ``os.environ.get("APP_MODE)``
  - Visualizar variables de entorno y su contenido (desde la terminal):
    - ``printenv``
    - ``echo $VAR``
  - Revertir el valor de una variable de entorno:
    - ``unset VAR``
  - Configurar y revertir una variable de entorno de Linux desde la línea de comandos afecta solo tus sesiones actuales. Si deseas que la configuración se mantenga en todos los inicios de sesión, debes definir las variables de entorno en tu archivo de inicialización personal, es decir ``.bash_profile.``

- Archivo .env
  - para reunir en este archivo todas nuestras variables de entorno
  - RECUERDA! excluirlo del git poniendolo en .ignore
  - para usarlo en los archivos python debemos instalar la libreria python-dotenv: ``pip install python-dotenv`` e importar con ``from dotenv import load_dotenv``
  - lo usaremos con ``load_dotenv(".env")``

## Configuración de Servidores en la Nube para Despliegue

### 6 Fundamentos de servidores y conexión por SSH

    Fundamentos de servidores y conexión por SSH
    03:33 minutos

- instancias de servidor en la nube
- CPU, RAM, almacenamiento
- IP
- accceso al servidor con SSH
- crear una cuenta en AWS (free tier)
  - **!!! revisar video para crear cuenta gratuita**
- instancias de computo ``ec2``

### 7 Creación y configuración de instancias en AWS, Linode y DigitalOcean

    Creación y configuración de instancias en AWS, Linode y DigitalOcean
    07:17 minutos

Lecturas recomendadas

- [Crear una instancia EC2 en AWS](<https://aws.amazon.com/es/getting-started/hands-on/deploy-wordpress-with-amazon-rds/3/>)

### 8 Creación de instancias en AWS

    Creación de instancias en AWS
    12:44 minutos

### 9 Configuración de SSH
    Configuración de SSH
    08:41 minutos

10
Instalación y gestión de paquetes en el servidor
Instalación y gestión de paquetes en el servidor
10:13 minutos

11
Configuración de DNS para dominios en despliegue
Configuración de DNS para dominios en despliegue
13:55 minutos

12
Certificados SSL con Let’s Encrypt para seguridad en producción

    Certificados SSL con Let’s Encrypt para seguridad en producción
    05:16 minutos

Administración y Optimización de Servidores para Producción

    13
    Configuración de servidores web y aplicaciones con WSGI y ASGI

Configuración de servidores web y aplicaciones con WSGI y ASGI
14:41 minutos

### 14 ¿Cómo configurar UWSGI con Python y NginX en producción?

    ¿Cómo configurar UWSGI con Python y NginX en producción?
    14:34 minutos

Lecturas recomendadas

- [uWSGI — Documentación de Flask (3.0.x)](<https://flask.palletsprojects.com/es/latest/deploying/uwsgi/>)

15
Configuración de Proxy Reverso en Nginx para Aplicaciones WSGI
Configuración de Proxy Reverso en Nginx para Aplicaciones WSGI
04:33 minutos

16
Manejo de errores y configuración de logs en producción
Manejo de errores y configuración de logs en producción
11:49 minutos

17
Monitoreo de aplicaciones Python en producción usando Sentry
Monitoreo de aplicaciones Python en producción usando Sentry
08:54 minutos

18
¿Cómo configurar un archivo .env en Django para producción?

    ¿Cómo configurar un archivo .env en Django para producción?
    04:28 minutos

Integración de Servicios Complementarios para Aplicaciones Python

    19
    Configuración de Bases de Datos PostgreSQL en el Servidor de la Aplicación

Configuración de Bases de Datos PostgreSQL en el Servidor de la Aplicación
08:20 minutos

20
Configuración de Bases de Datos en Producción con Amazon RDS
Configuración de Bases de Datos en Producción con Amazon RDS
11:47 minutos

21
Servicios para archivos estáticos (S3, Cloudflare)

    Servicios para archivos estáticos (S3, Cloudflare)
    06:05 minutos

Automatización y CI/CD para Despliegues Python

    22
    Automatización de despliegue con Ansible

Automatización de despliegue con Ansible
11:39 minutos

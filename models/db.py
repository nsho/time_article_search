# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
# AppConfig configuration made easy. Look inside private/appconfig.ini
# Auth is for authenticaiton and access control
# -------------------------------------------------------------------------
from gluon.contrib.appconfig import AppConfig
from gluon.tools import Auth

# -------------------------------------------------------------------------
# This scaffolding model makes your app work on Google App Engine too
# File is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

if request.global_settings.web2py_version < "2.15.5":
    raise HTTP(500, "Requires web2py 2.15.5 or newer")

# -------------------------------------------------------------------------
# if SSL/HTTPS is properly configured and you want all HTTP requests to
# be redirected to HTTPS, uncomment the line below:
# -------------------------------------------------------------------------
# request.requires_https()

# -------------------------------------------------------------------------
# once in production, remove reload=True to gain full speed
# -------------------------------------------------------------------------
configuration = AppConfig(reload=True)

if not request.env.web2py_runtime_gae:
    # ---------------------------------------------------------------------
    # if NOT running on Google App Engine use SQLite or other DB
    # ---------------------------------------------------------------------
    db = DAL(configuration.get('db.uri'),
             pool_size=configuration.get('db.pool_size'),
             migrate_enabled=configuration.get('db.migrate'),
             check_reserved=['all'])
else:
    # ---------------------------------------------------------------------
    # connect to Google BigTable (optional 'google:datastore://namespace')
    # ---------------------------------------------------------------------
    db = DAL('google:datastore+ndb')
    # ---------------------------------------------------------------------
    # store sessions and tickets there
    # ---------------------------------------------------------------------
    session.connect(request, response, db=db)
    # ---------------------------------------------------------------------
    # or store session in Memcache, Redis, etc.
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db = MEMDB(Client()))
    # ---------------------------------------------------------------------

# -------------------------------------------------------------------------
# by default give a view/generic.extension to all actions from localhost
# none otherwise. a pattern can be 'controller/function.extension'
# -------------------------------------------------------------------------
response.generic_patterns = []
if request.is_local and not configuration.get('app.production'):
    response.generic_patterns.append('*')

# -------------------------------------------------------------------------
# choose a style for forms
# -------------------------------------------------------------------------
response.formstyle = 'bootstrap4_inline'
response.form_label_separator = ''

# -------------------------------------------------------------------------
# (optional) optimize handling of static files
# -------------------------------------------------------------------------
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

# -------------------------------------------------------------------------
# (optional) static assets folder versioning
# -------------------------------------------------------------------------
# response.static_version = '0.0.0'

# -------------------------------------------------------------------------
# Here is sample code if you need for
# - email capabilities
# - authentication (registration, login, logout, ... )
# - authorization (role based authorization)
# - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
# - old style crud actions
# (more options discussed in gluon/tools.py)
# -------------------------------------------------------------------------

# host names must be a list of allowed host names (glob syntax allowed)
auth = Auth(db, host_names=configuration.get('host.names'))

# -------------------------------------------------------------------------
# create all tables needed by auth, maybe add a list of extra fields
# -------------------------------------------------------------------------
auth.settings.extra_fields['auth_user'] = []
auth.define_tables(username=False, signature=False)

# -------------------------------------------------------------------------
# configure email
# -------------------------------------------------------------------------
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else configuration.get('smtp.server')
mail.settings.sender = configuration.get('smtp.sender')
mail.settings.login = configuration.get('smtp.login')
mail.settings.tls = configuration.get('smtp.tls') or False
mail.settings.ssl = configuration.get('smtp.ssl') or False

# -------------------------------------------------------------------------
# configure auth policy
# -------------------------------------------------------------------------
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

# -------------------------------------------------------------------------
# read more at http://dev.w3.org/html5/markup/meta.name.html
# -------------------------------------------------------------------------
response.meta.author = configuration.get('app.author')
response.meta.description = configuration.get('app.description')
response.meta.keywords = configuration.get('app.keywords')
response.meta.generator = configuration.get('app.generator')
response.show_toolbar = configuration.get('app.toolbar')

# -------------------------------------------------------------------------
# your http://google.com/analytics id
# -------------------------------------------------------------------------
response.google_analytics_id = configuration.get('google.analytics_id')

# -------------------------------------------------------------------------
# maybe use the scheduler
# -------------------------------------------------------------------------
if configuration.get('scheduler.enabled'):
    from gluon.scheduler import Scheduler
    scheduler = Scheduler(db, heartbeat=configuration.get('scheduler.heartbeat'))

# -------------------------------------------------------------------------
# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.
#
# More API examples for controllers:
#
# >>> db.mytable.insert(myfield='value')
# >>> rows = db(db.mytable.myfield == 'value').select(db.mytable.ALL)
# >>> for row in rows: print row.id, row.myfield
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# after defining tables, uncomment below to enable auditing
# -------------------------------------------------------------------------
# auth.enable_record_versioning(db)

db = DAL('sqlite://storage.sqlite')

db.define_table('corpus',
                Field('docID'),
                Field('date'),
                Field('page'),
                Field('text')
                )

db.define_table('queries',
                Field('query', requires = IS_NOT_EMPTY())
                )

db.define_table('td_tfidf_a',
                Field('stem', requires = IS_NOT_EMPTY()),
                Field('doc17'),	Field('doc18'),	Field('doc19'),	Field('doc20'),	Field('doc21'),	Field('doc23'),	Field('doc24'),	Field('doc25'),	Field('doc26'),	Field('doc27'),	Field('doc28'),	Field('doc29'),	Field('doc30'),	Field('doc31'),	Field('doc32'),	Field('doc33'),	Field('doc34'),	Field('doc35'),	Field('doc36'),	Field('doc40'),	Field('doc42'),	Field('doc43'),	Field('doc45'),	Field('doc47'),	Field('doc48'),	Field('doc49'),	Field('doc50'),	Field('doc51'),	Field('doc52'),	Field('doc53'),	Field('doc54'),	Field('doc55'),	Field('doc57'),	Field('doc58'),	Field('doc59'),	Field('doc60'),	Field('doc61'),	Field('doc62'),	Field('doc63'),	Field('doc64'),	Field('doc65'),	Field('doc66'),	Field('doc67'),	Field('doc68'),	Field('doc69'),	Field('doc70'),	Field('doc71'),	Field('doc72'),	Field('doc81'),	Field('doc82'),	Field('doc83'),	Field('doc84'),	Field('doc85'),	Field('doc86'),	Field('doc87'),	Field('doc88'),	Field('doc90'),	Field('doc91'),	Field('doc92'),	Field('doc93'),	Field('doc94'),	Field('doc95'),	Field('doc96'),	Field('doc97'),	Field('doc98'),	Field('doc99'),	Field('doc100'),	Field('doc101'),	Field('doc102'),	Field('doc104'),	Field('doc105'),	Field('doc106'),	Field('doc107'),	Field('doc108'),	Field('doc109'),	Field('doc110'),	Field('doc111'),	Field('doc112'),	Field('doc113'),	Field('doc115'),	Field('doc116'),	Field('doc117'),	Field('doc118'),	Field('doc119'),	Field('doc120'),	Field('doc121'),	Field('doc122'),	Field('doc123'),	Field('doc126'),	Field('doc128'),	Field('doc129'),	Field('doc130'),	Field('doc131'),	Field('doc133'),	Field('doc134'),	Field('doc135'),	Field('doc136'),	Field('doc137'),	Field('doc138'),	Field('doc140'),	Field('doc143'),	Field('doc144'),	Field('doc145'),	Field('doc146'),	Field('doc147'),	Field('doc148'),	Field('doc149'),	Field('doc150'),	Field('doc151'),	Field('doc152'),	Field('doc153'),	Field('doc154'),	Field('doc155'),	Field('doc156'),	Field('doc157'),	Field('doc158'),	Field('doc159'),	Field('doc160'),	Field('doc161'),	Field('doc162'),	Field('doc163'),	Field('doc170'),	Field('doc171'),	Field('doc172'),	Field('doc173'),	Field('doc174'),	Field('doc175'),	Field('doc176'),	Field('doc177'),	Field('doc178'),	Field('doc179'),	Field('doc180'),	Field('doc181'),	Field('doc182'),	Field('doc183'),	Field('doc184'),	Field('doc185'),	Field('doc186'),	Field('doc187'),	Field('doc188'),	Field('doc189'),	Field('doc190'),	Field('doc191'),	Field('doc192'),	Field('doc193'),	Field('doc194'),	Field('doc195'),	Field('doc196'),	Field('doc197'),	Field('doc198'),	Field('doc199'),	Field('doc200'),	Field('doc201'),	Field('doc202'),	Field('doc203'),	Field('doc204'),	Field('doc213'),	Field('doc214'),	Field('doc215'),	Field('doc217'),	Field('doc218'),	Field('doc219'),	Field('doc220'),	Field('doc221'),	Field('doc222'),	Field('doc223'),	Field('doc224'),	Field('doc225'),	Field('doc226'),	Field('doc227'),	Field('doc228'),	Field('doc229'),	Field('doc230'),	Field('doc231'),	Field('doc232'),	Field('doc234'),	Field('doc235'),	Field('doc236'),	Field('doc237'),	Field('doc238'),	Field('doc239'),	Field('doc240'),	Field('doc241'),	Field('doc242'),	Field('doc243'),	Field('doc244'),	Field('doc245'),	Field('doc246'),	Field('doc247'),	Field('doc248'),	Field('doc249'),	Field('doc250'),	Field('doc251'),	Field('doc252'),	Field('doc253'),	Field('doc254'),	Field('doc255'),	Field('doc256'),	Field('doc257'),	Field('doc258'),	Field('doc259'),	Field('doc260'),	Field('doc261')
                )

#named B  as it is the second half of tfidf table for a above.

db.define_table('td_tfidfB',
                Field('stem', requires = IS_NOT_EMPTY()),
Field('doc262'),	Field('doc263'),	Field('doc264'),	Field('doc265'),	Field('doc266'),	Field('doc267'),	Field('doc268'),	Field('doc269'),	Field('doc270'),	Field('doc272'),	Field('doc273'),	Field('doc274'),	Field('doc275'),	Field('doc276'),	Field('doc277'),	Field('doc278'),	Field('doc279'),	Field('doc280'),	Field('doc281'),	Field('doc282'),	Field('doc283'),	Field('doc284'),	Field('doc285'),	Field('doc286'),	Field('doc287'),	Field('doc288'),	Field('doc289'),	Field('doc292'),	Field('doc293'),	Field('doc294'),	Field('doc295'),	Field('doc296'),	Field('doc297'),	Field('doc298'),	Field('doc299'),	Field('doc300'),	Field('doc301'),	Field('doc302'),	Field('doc303'),	Field('doc304'),	Field('doc305'),	Field('doc306'),	Field('doc307'),	Field('doc308'),	Field('doc309'),	Field('doc310'),	Field('doc311'),	Field('doc312'),	Field('doc313'),	Field('doc315'),	Field('doc317'),	Field('doc318'),	Field('doc319'),	Field('doc320'),	Field('doc321'),	Field('doc322'),	Field('doc323'),	Field('doc324'),	Field('doc326'),	Field('doc329'),	Field('doc330'),	Field('doc331'),	Field('doc332'),	Field('doc333'),	Field('doc334'),	Field('doc335'),	Field('doc336'),	Field('doc337'),	Field('doc341'),	Field('doc342'),	Field('doc345'),	Field('doc346'),	Field('doc347'),	Field('doc348'),	Field('doc350'),	Field('doc351'),	Field('doc353'),	Field('doc354'),	Field('doc355'),	Field('doc356'),	Field('doc357'),	Field('doc358'),	Field('doc359'),	Field('doc361'),	Field('doc363'),	Field('doc364'),	Field('doc365'),	Field('doc367'),	Field('doc368'),	Field('doc369'),	Field('doc370'),	Field('doc380'),	Field('doc381'),	Field('doc382'),	Field('doc383'),	Field('doc384'),	Field('doc385'),	Field('doc386'),	Field('doc388'),	Field('doc389'),	Field('doc390'),	Field('doc391'),	Field('doc392'),	Field('doc394'),	Field('doc396'),	Field('doc398'),	Field('doc399'),	Field('doc400'),	Field('doc401'),	Field('doc402'),	Field('doc403'),	Field('doc404'),	Field('doc405'),	Field('doc406'),	Field('doc407'),	Field('doc408'),	Field('doc411'),	Field('doc412'),	Field('doc413'),	Field('doc414'),	Field('doc415'),	Field('doc417'),	Field('doc418'),	Field('doc422'),	Field('doc424'),	Field('doc425'),	Field('doc426'),	Field('doc427'),	Field('doc430'),	Field('doc431'),	Field('doc434'),	Field('doc436'),	Field('doc437'),	Field('doc438'),	Field('doc442'),	Field('doc443'),	Field('doc444'),	Field('doc445'),	Field('doc446'),	Field('doc449'),	Field('doc459'),	Field('doc460'),	Field('doc461'),	Field('doc462'),	Field('doc463'),	Field('doc464'),	Field('doc470'),	Field('doc471'),	Field('doc472'),	Field('doc473'),	Field('doc475'),	Field('doc476'),	Field('doc477'),	Field('doc478'),	Field('doc479'),	Field('doc480'),	Field('doc485'),	Field('doc487'),	Field('doc490'),	Field('doc491'),	Field('doc492'),	Field('doc493'),	Field('doc494'),	Field('doc495'),	Field('doc496'),	Field('doc497'),	Field('doc498'),	Field('doc501'),	Field('doc502'),	Field('doc503'),	Field('doc504'),	Field('doc507'),	Field('doc508'),	Field('doc509'),	Field('doc511'),	Field('doc512'),	Field('doc513'),	Field('doc514'),	Field('doc516'),	Field('doc518'),	Field('doc519'),	Field('doc521'),	Field('doc522'),	Field('doc523'),	Field('doc524'),	Field('doc525'),	Field('doc526'),	Field('doc527'),	Field('doc528'),	Field('doc529'),	Field('doc530'),	Field('doc533'),	Field('doc534'),	Field('doc535'),	Field('doc536'),	Field('doc537'),	Field('doc538'),	Field('doc539'),	Field('doc540'),	Field('doc541'),	Field('doc542'),	Field('doc543'),	Field('doc544'),	Field('doc545'),	Field('doc546'),	Field('doc548'),	Field('doc549'),	Field('doc550'),	Field('doc551'),	Field('doc552'),	Field('doc553'),	Field('doc555'),	Field('doc556'),	Field('doc557'),	Field('doc558'),	Field('doc559'),	Field('doc560'),	Field('doc561'),	Field('doc562'),	Field('doc563')
)

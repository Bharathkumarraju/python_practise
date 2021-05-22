bharathdasaraju@MacBook-Pro python_practise (main) $ pip install requests==2.21.0
Collecting requests==2.21.0
  Downloading https://files.pythonhosted.org/packages/7d/e3/20f3d364d6c8e5d2353c72a67778eb189176f08e873c9900e10c0287b84b/requests-2.21.0-py2.py3-none-any.whl (57kB)
     |████████████████████████████████| 61kB 760kB/s
Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.7/site-packages (from requests==2.21.0) (2019.6.16)
Collecting urllib3<1.25,>=1.21.1 (from requests==2.21.0)
  Downloading https://files.pythonhosted.org/packages/01/11/525b02e4acc0c747de8b6ccdab376331597c569c42ea66ab0a1dbd36eca2/urllib3-1.24.3-py2.py3-none-any.whl (118kB)
     |████████████████████████████████| 122kB 1.4MB/s
Requirement already satisfied: idna<2.9,>=2.5 in /usr/local/lib/python3.7/site-packages (from requests==2.21.0) (2.8)
Requirement already satisfied: chardet<3.1.0,>=3.0.2 in /usr/local/lib/python3.7/site-packages (from requests==2.21.0) (3.0.4)
ERROR: botocore 1.20.32 has requirement urllib3<1.27,>=1.25.4, but you'll have urllib3 1.24.3 which is incompatible.
Installing collected packages: urllib3, requests
  Found existing installation: urllib3 1.26.4
    Uninstalling urllib3-1.26.4:
      Successfully uninstalled urllib3-1.26.4
  Found existing installation: requests 2.25.1
    Uninstalling requests-2.25.1:
      Successfully uninstalled requests-2.25.1
Successfully installed requests-2.21.0 urllib3-1.24.3
bharathdasaraju@MacBook-Pro python_practise (main) $

=====================================================================================================================================================================


/usr/local/bin/python3.7 /Users/bharathdasaraju/git/python_practise/Day18_May22_2021/pandas/demo_pip_pulumi.py
Provider
ProviderArgs
ProviderBatchingArgs
__builtins__
__cached__
__doc__
__file__
__loader__
__name__
__package__
__path__
__spec__
_inputs
_register_module
_utilities
accesscontextmanager
activedirectory
apigateway
apigee
appengine
artifactregistry
bigquery
bigtable
billing
binaryauthorization
certificateauthority
cloudasset
cloudbuild
cloudfunctions
cloudidentity
cloudrun
cloudscheduler
cloudtasks
composer
compute
config
container
containeranalysis
datacatalog
dataflow
datafusion
dataloss
dataproc
datastore
deploymentmanager
diagflow
dns
endpoints
essentialcontacts
eventarc
filestore
firebase
firestore
folder
gameservices
gkehub
healthcare
iam
iap
identityplatform
iot
kms
logging
memcache
ml
monitoring
networkmanagement
notebooks
organizations
osconfig
oslogin
outputs
projects
provider
pubsub
redis
resourcemanager
runtimeconfig
secretmanager
securitycenter
serviceaccount
servicedirectory
servicenetworking
serviceusage
sourcerepo
spanner
sql
storage
tags
tpu
vpcaccess
workflows
---------------------------
ConfigFile
ConfigGroup
Directory
Provider
ProviderArgs
__builtins__
__cached__
__doc__
__file__
__loader__
__name__
__package__
__path__
__spec__
_tables
_utilities
admissionregistration
apiextensions
apiregistration
apps
auditregistration
authentication
authorization
autoscaling
batch
certificates
coordination
core
discovery
events
extensions
flowcontrol
helm
kustomize
meta
networking
node
policy
provider
rbac
scheduling
settings
storage
typing
yaml

Process finished with exit code 0


================================================================================================================================:

bharathdasaraju@MacBook-Pro python_practise (main) $ pip list
Package                                 Version
--------------------------------------- ---------
alabaster                               0.7.12
altgraph                                0.17
ansible                                 2.9.1
appnope                                 0.1.0
argcomplete                             1.12.3
Arpeggio                                1.10.2
asgiref                                 3.3.4
asn1crypto                              0.24.0
attrs                                   19.3.0
awscli                                  1.19.32
Babel                                   2.8.0
backcall                                0.1.0
bleach                                  3.1.3
boto                                    2.49.0
boto3                                   1.17.32
botocore                                1.20.32
certifi                                 2019.6.16
cffi                                    1.12.3
chardet                                 3.0.4
Click                                   7.0
colorama                                0.3.9
crcmod                                  1.7
cryptography                            3.4.7
cycler                                  0.10.0
decorator                               4.4.2
defusedxml                              0.6.0
dill                                    0.3.3
Django                                  3.2.3
docutils                                0.14
entrypoints                             0.3
fasteners                               0.16
Flask                                   1.1.1
gcloud                                  0.18.3
gcs-oauth2-boto-plugin                  2.7
google-apitools                         0.5.31
google-reauth                           0.1.1
googleapis-common-protos                1.53.0
grpcio                                  1.37.1
gsutil                                  4.61
httplib2                                0.19.1
idna                                    2.8
imagesize                               1.2.0
importlib-metadata                      1.5.0
ipykernel                               5.2.0
ipython                                 7.13.0
ipython-genutils                        0.2.0
ipywidgets                              7.5.1
itsdangerous                            1.1.0
jedi                                    0.16.0
Jinja2                                  2.10.1
jmespath                                0.9.4
jsonschema                              3.2.0
jupyter                                 1.0.0
jupyter-client                          6.1.0
jupyter-console                         6.1.0
jupyter-core                            4.6.3
kiwisolver                              1.3.1
lxml                                    4.4.1
macholib                                1.14
MarkupSafe                              1.1.1
matplotlib                              3.4.1
mistune                                 0.8.4
mock                                    2.0.0
monotonic                               1.6
MouseInfo                               0.1.2
mysql                                   0.0.2
mysql-connector-python                  8.0.20
mysqlclient                             1.4.6
nbconvert                               5.6.1
nbformat                                5.0.4
notebook                                6.0.3
numpy                                   1.20.2
oauth2client                            4.1.3
packaging                               20.0
pandas                                  1.2.4
pandocfilters                           1.4.2
parso                                   0.6.2
parver                                  0.3.1
pathspec                                0.5.9
pbr                                     5.6.0
pexpect                                 4.8.0
pickleshare                             0.7.5
Pigments                                1.6
Pillow                                  6.2.1
pip                                     19.1.1
powerline-status                        2.7
prometheus-client                       0.7.1
prompt-toolkit                          3.0.4
protobuf                                3.12.0
ptyprocess                              0.6.0
pulumi                                  3.1.0
pulumi-gcp                              5.2.0
pulumi-kubernetes                       3.1.2
pulumi-random                           4.1.1
pyasn1                                  0.4.6
pyasn1-modules                          0.2.8
PyAutoGUI                               0.9.48
pybase64                                1.0.1
pycparser                               2.19
PyGetWindow                             0.0.7
Pygments                                2.4.2
pyinstaller                             4.3
pyinstaller-hooks-contrib               2021.1
PyMsgBox                                1.0.7
PyMySQL                                 0.9.3
PyNaCl                                  1.3.0
pyobjc                                  6.1
pyobjc-core                             6.1
pyobjc-framework-Accounts               6.1
pyobjc-framework-AddressBook            6.1
pyobjc-framework-AdSupport              6.1
pyobjc-framework-AppleScriptKit         6.1
pyobjc-framework-AppleScriptObjC        6.1
pyobjc-framework-ApplicationServices    6.1
pyobjc-framework-Automator              6.1
pyobjc-framework-AVFoundation           6.1
pyobjc-framework-AVKit                  6.1
pyobjc-framework-BusinessChat           6.1
pyobjc-framework-CalendarStore          6.1
pyobjc-framework-CFNetwork              6.1
pyobjc-framework-CloudKit               6.1
pyobjc-framework-Cocoa                  6.1
pyobjc-framework-Collaboration          6.1
pyobjc-framework-ColorSync              6.1
pyobjc-framework-Contacts               6.1
pyobjc-framework-ContactsUI             6.1
pyobjc-framework-CoreAudio              6.1
pyobjc-framework-CoreAudioKit           6.1
pyobjc-framework-CoreBluetooth          6.1
pyobjc-framework-CoreData               6.1
pyobjc-framework-CoreLocation           6.1
pyobjc-framework-CoreMedia              6.1
pyobjc-framework-CoreMediaIO            6.1
pyobjc-framework-CoreML                 6.1
pyobjc-framework-CoreServices           6.1
pyobjc-framework-CoreSpotlight          6.1
pyobjc-framework-CoreText               6.1
pyobjc-framework-CoreWLAN               6.1
pyobjc-framework-CryptoTokenKit         6.1
pyobjc-framework-DictionaryServices     6.1
pyobjc-framework-DiscRecording          6.1
pyobjc-framework-DiscRecordingUI        6.1
pyobjc-framework-DiskArbitration        6.1
pyobjc-framework-DVDPlayback            6.1
pyobjc-framework-EventKit               6.1
pyobjc-framework-ExceptionHandling      6.1
pyobjc-framework-ExternalAccessory      6.1
pyobjc-framework-FinderSync             6.1
pyobjc-framework-FSEvents               6.1
pyobjc-framework-GameCenter             6.1
pyobjc-framework-GameController         6.1
pyobjc-framework-GameKit                6.1
pyobjc-framework-GameplayKit            6.1
pyobjc-framework-ImageCaptureCore       6.1
pyobjc-framework-IMServicePlugIn        6.1
pyobjc-framework-InputMethodKit         6.1
pyobjc-framework-InstallerPlugins       6.1
pyobjc-framework-InstantMessage         6.1
pyobjc-framework-Intents                6.1
pyobjc-framework-IOSurface              6.1
pyobjc-framework-iTunesLibrary          6.1
pyobjc-framework-LatentSemanticMapping  6.1
pyobjc-framework-LaunchServices         6.1
pyobjc-framework-libdispatch            6.1
pyobjc-framework-LocalAuthentication    6.1
pyobjc-framework-MapKit                 6.1
pyobjc-framework-MediaAccessibility     6.1
pyobjc-framework-MediaLibrary           6.1
pyobjc-framework-MediaPlayer            6.1
pyobjc-framework-MediaToolbox           6.1
pyobjc-framework-MetalKit               6.1
pyobjc-framework-ModelIO                6.1
pyobjc-framework-MultipeerConnectivity  6.1
pyobjc-framework-NaturalLanguage        6.1
pyobjc-framework-NetFS                  6.1
pyobjc-framework-Network                6.1
pyobjc-framework-NetworkExtension       6.1
pyobjc-framework-NotificationCenter     6.1
pyobjc-framework-OpenDirectory          6.1
pyobjc-framework-OSAKit                 6.1
pyobjc-framework-Photos                 6.1
pyobjc-framework-PhotosUI               6.1
pyobjc-framework-PreferencePanes        6.1
pyobjc-framework-PubSub                 6.1
pyobjc-framework-QTKit                  6.1
pyobjc-framework-Quartz                 6.1
pyobjc-framework-SafariServices         6.1
pyobjc-framework-SceneKit               6.1
pyobjc-framework-ScreenSaver            6.1
pyobjc-framework-ScriptingBridge        6.1
pyobjc-framework-SearchKit              6.1
pyobjc-framework-Security               6.1
pyobjc-framework-SecurityFoundation     6.1
pyobjc-framework-SecurityInterface      6.1
pyobjc-framework-ServiceManagement      6.1
pyobjc-framework-Social                 6.1
pyobjc-framework-SpriteKit              6.1
pyobjc-framework-StoreKit               6.1
pyobjc-framework-SyncServices           6.1
pyobjc-framework-SystemConfiguration    6.1
pyobjc-framework-UserNotifications      6.1
pyobjc-framework-VideoSubscriberAccount 6.1
pyobjc-framework-VideoToolbox           6.1
pyobjc-framework-Vision                 6.1
pyobjc-framework-WebKit                 6.1
pyOpenSSL                               20.0.1
pyparsing                               2.4.6
pyperclip                               1.7.0
PyRect                                  0.1.4
pyrsistent                              0.16.0
PyScreeze                               0.1.25
python-dateutil                         2.8.0
PyTweening                              1.0.3
pytz                                    2019.3
pyu2f                                   0.1.5
PyYAML                                  5.4.1
pyzmq                                   19.0.0
qtconsole                               4.7.1
QtPy                                    1.9.0
requests                                2.21.0
retry-decorator                         1.1.1
rsa                                     3.4.2
s3transfer                              0.3.6
selenium                                3.141.0
semver                                  2.13.0
Send2Trash                              1.5.0
setuptools                              41.0.1
six                                     1.15.0
snowballstemmer                         2.0.0
Sphinx                                  2.3.1
sphinx-rtd-theme                        0.4.3
sphinxcontrib-applehelp                 1.0.1
sphinxcontrib-devhelp                   1.0.1
sphinxcontrib-htmlhelp                  1.0.2
sphinxcontrib-jsmath                    1.0.1
sphinxcontrib-qthelp                    1.0.2
sphinxcontrib-serializinghtml           1.1.3
sqlparse                                0.4.1
terminado                               0.8.3
testpath                                0.4.4
tk                                      0.1.0
tornado                                 6.0.4
traitlets                               4.3.3
typing-extensions                       3.10.0.0
urllib3                                 1.24.3
wcwidth                                 0.1.9
webencodings                            0.5.1
Werkzeug                                0.15.6
wheel                                   0.33.4
widgetsnbextension                      3.5.1
yamllint                                1.16.0
zipp                                    3.1.0
bharathdasaraju@MacBook-Pro python_practise (main) $


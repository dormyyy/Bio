from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = "5005663498:AAGK0RPXFXndmDuFRXDT_432RDgixLgTslQ"
ADMINS = ['585013942']
IP = "127.0.0.1"
PGUSER = "postgres"
DBNAME = ""
PGPASSWORD = ""
DBPORT = 5432

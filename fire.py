



from libs.clean_data import *


CleanDataClass = CleanData()
CleanDataClass.login()
CleanDataClass.create_missing_data(
    company="Edward Jones",
    type="Roth 401k"
)

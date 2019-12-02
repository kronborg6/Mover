import os
import os.path
from datetime import datetime
# Flytter er den mapp
flytter = '(but den sti hvor de filler som skal flyttes er)'
run = True
now = datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")
date = year + "-" + month + "-" + day

def file_system(extensions_folders, flytter, date, month, year, month_name):

    for filename in os.listdir(flytter):
        i = 1
        if filename != '.DS_Store':

            name = filename
            name_whit_out_extension = os.path.splitext(name)[0]
            name_extension = os.path.splitext(name)[1]

            folder_destination_path = extensions_folders[name_whit_out_extension]

            new_name = name_whit_out_extension + " " + date + name_extension

            if name_whit_out_extension == name_whit_out_extension:

                year_exists = False
                month_exists = False

                for folder_name in os.listdir(extensions_folders[name_whit_out_extension]):
                    if folder_name == year:
                        folder_destination_path = extensions_folders[name_whit_out_extension] + "/" + year
                        year_exists = True

                        for folder_month in os.listdir(folder_destination_path):

                            month_f = month_name[month]

                            if month_f == folder_month:
                                folder_destination_path = extensions_folders[name_whit_out_extension] + "/" + year + "/" + month_f
                                month_exists = True

                if not year_exists:
                    os.mkdir(extensions_folders[name_whit_out_extension] + "/" + year)
                    folder_destination_path = extensions_folders[name_whit_out_extension] + "/" + year

                if not month_exists:
                    month_f = month_name[month]
                    os.mkdir(extensions_folders[name_whit_out_extension] + "/" + year + "/" + month_f)
                    folder_destination_path = extensions_folders[name_whit_out_extension] + "/" + year + "/" + month_f


                new_name = name_whit_out_extension + " " + str(i) + " " + date + name_extension
                file_exsits = os.path.isfile(folder_destination_path + "/" + new_name)
                folder_destination_path_2 = folder_destination_path + "/" + new_name
                while file_exsits:
                    i += 1
                    new_name = name_whit_out_extension + " " + str(i) + " " + date + name_extension
                    file_exsits = os.path.isfile(folder_destination_path + "/" + new_name)
                    folder_destination_path_2 = folder_destination_path + "/" + new_name

                src = flytter + "/" + filename
                os.rename(src, folder_destination_path_2)


extensions_folders = {


    '(navet på den fil som skal flyttes)': "(der hvor de filer med det navn skal hend)",
    '(navet på den fil som skal flyttes)': "(der hvor de filer med det navn skal hend)",
    '(navet på den fil som skal flyttes)': "(der hvor de filer med det navn skal hend)",
    '(navet på den fil som skal flyttes)': "(der hvor de filer med det navn skal hend)",
    '(navet på den fil som skal flyttes)': "(der hvor de filer med det navn skal hend)",
    '(navet på den fil som skal flyttes)': "(der hvor de filer med det navn skal hend)",



}
month_name = {
    '1': "Jan",
    '2': "Feb",
    '3': "Mar",
    '4': "Apr",
    '5': "Maj",
    '6': "Jun",
    '7': "Jul",
    '8': "Aug",
    '9': "Sep",
    '10': "Okt",
    '11': "Nov",
    '12': "Dec",
}

while run:
    file_system(extensions_folders, flytter, date, month, year, month_name)

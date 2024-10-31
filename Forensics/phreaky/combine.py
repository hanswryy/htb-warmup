# combine all pdf part in attachment/phreaks_plan into one file
import os

# open the file
with open("attachment/phreaks_plan_main", "wb") as file:
    # loop through all the parts
    for i in range(1, 16):
        # open the part file
        with open(f"attachment/phreaks_plan/phreaks_plan.pdf.part{i}", "rb") as part_file:
            # read the part file
            part = part_file.read()
            # write the part file to the main file
            file.write(part)

# write file to pdf
os.rename("attachment/phreaks_plan_main", "attachment/phreaks_plan.pdf")
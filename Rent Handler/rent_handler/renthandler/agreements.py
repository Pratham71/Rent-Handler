"""A Python Module Made to Generate Agreements According to Tenants"""

"""
Structure of JSON data:
{
  "Address": "Pratham Nagpal son of Mr.Harbans Nagpal resident of Malviya Nagar New Delhi",
  "Adhaar": "5000 5000 5000",
  "Age": "12",
  "Block Name": "A4",
  "Contact Number": "9599271867",
  "DOB": "2024-04-11",
  "Gender": "Male",
  "Leasing Month Year": "2024-04",
  "amt": "9000",
  "leaseFrom": "2024-04-11",
  "leaseTo": "2024-04-23",
  "name": "Pratham Nagpal"
}
"""

import shutil,os
from bs4 import BeautifulSoup
from num2words import num2words

months = {'01': 'January', 
          '02': 'February', 
          '03': 'March', 
          '04': 'April', 
          '05': 'May', 
          '06': 'June', 
          '07': 'July', 
          '08': 'August', 
          '09': 'September', 
          '10': 'October', 
          '11': 'November', 
          '12': 'December'
        }



class Agreements_Generator:
  def __init__(self,data:dict[str,str]):
    self.cwd=os.getcwd()
    self.data = data
    self.path_to_template = r"C:\Users\Pratham\Desktop\Rent Handler\rent_handler\agreements\template\RentTemplate.html"
    self.path_to_agreement_dir = r"C:\Users\Pratham\Desktop\Rent Handler\rent_handler\agreements" #r"rent_handler\agreements"
    self.tags_of_temp ={"Block Name":"Block Name","Month Year":"Month Year","Person Info":"person info","AMT":"amt","AMT IN WORDS":"amt in words","from":"from","to":"to","initial_rent_amt":"initial_rent_amt","initial_rent_amt_in_words":"initial_rent_amt_in_words"}
    self.tags_of_add ={'Address': 'Address', 'Adhaar': 'Adhaar', 'Age': 'Age', 'Block Name': 'Block Name', 'Contact Number': 'Contact Number', 'DOB': 'DOB', 'Gender': 'Gender', 'Leasing Month Year': 'Leasing Month Year', 'amt': 'amt', 'leaseFrom': 'leaseFrom', 'leaseTo': 'leaseTo', 'name': 'name'}

  def _copy(self):
    HTML_FILE_NAME=self.data["name"]+"_details"+"\\"+self.data[self.tags_of_add["name"]]+"_Agreement.html"

    soup = str(self._format())

    with open(HTML_FILE_NAME,"w") as html:
      html.write(soup)
    
    print(f"Copied HTML content from '{self.path_to_template}' ----> '{HTML_FILE_NAME}'\n")
  
  def _format(self):
    os.chdir(self.path_to_agreement_dir)
    with open(self.path_to_template,"r") as temp_html:
      soup = BeautifulSoup(temp_html,"html.parser")

      BLOCK = soup.find("span",id=self.tags_of_temp["Block Name"]).string = self.data[self.tags_of_add["Block Name"]]

      year_month = self.data[self.tags_of_add["Leasing Month Year"]].split("-")
      new_year_month = months[year_month[1]]+"-"+year_month[0]

      Month_Year = soup.find("span",id=self.tags_of_temp["Month Year"]).string = new_year_month
      Person_Info = soup.find("span",id=self.tags_of_temp["Person Info"]).string = self.data[self.tags_of_add["Address"]]
      AMT = soup.find("span",id=self.tags_of_temp["AMT"]).string = "Rs."+self.data[self.tags_of_add["amt"]]
      AMT_IN_WORDS = soup.find("span",id=self.tags_of_temp["AMT IN WORDS"]).string = f' [{num2words(int(self.data[self.tags_of_add["amt"]]),lang="en_IN")+" Rupees only"}]'
      FROM = soup.find("span",id=self.tags_of_temp["from"]).string = self.data[self.tags_of_add["leaseFrom"]]
      TO = soup.find("span",id=self.tags_of_temp["to"]).string = self.data[self.tags_of_add["leaseTo"]]
      Initial_Amt = soup.find("span",id=self.tags_of_temp["initial_rent_amt"]).string = self.data[self.tags_of_add["amt"]]
      Initial_AMT_IN_WORDS = soup.find("span",id=self.tags_of_temp["initial_rent_amt_in_words"]).string = f' [{num2words(int(self.data[self.tags_of_add["amt"]]),lang="en_IN")+" Rupees only"}]'
      
    return soup.prettify()
  

  def Generate_Agreement(self):
    #Creating Specific Dir for Tenant
    os.chdir(self.path_to_agreement_dir)
    try:
      os.mkdir(self.data["name"]+"_details")
      print(f"Created Details Directory for '{self.data["name"]}'")
    except FileExistsError:
      print(f"Details Dir Already Exists for '{self.data["name"]}'\n")

    print("Creating Html i.e PDF FILE!")
    self._copy()

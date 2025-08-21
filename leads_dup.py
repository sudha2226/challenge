from util import print_log
import json

class LeadsDups(object):
    def __init__(self):
       with open("leads.json", "r") as f:
            data = json.load(f).get("leads")
            self.sorted_data = sorted(data, key=lambda x: (x['entryDate']), reverse=True)
            self.ids = {x.get("_id"): x for x in self.sorted_data}
 
          
    def changes(self):
        print_log("Function : changes")
        unique_leads = []
        seen_ids = set()
        seen_email = set()
        #print(self.parsed)
        for lead in self.sorted_data:
            #print(lead["_id"], lead["email"], lead["entryDate"])
            if lead["_id"] not in seen_ids:
                seen_ids.add(lead["_id"])
                if lead["email"] not in seen_email:
                    seen_email.add(lead["email"])
                    unique_leads.append(lead)

        result = {"leads": unique_leads}

        print_log("Final data with NO Duplicates")
        for lead in unique_leads:
            print_log(lead["_id"] + "  " + lead["email"] + "  " + lead["entryDate"])

    

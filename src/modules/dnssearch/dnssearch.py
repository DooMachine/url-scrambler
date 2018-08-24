import whois
class DomainNameCheck():
    """
    Domain Name Check Service
    """  

    def Check_Domains(self, domain_names, hostname_end):
        print ("Checking for domain avaliabilities")
        print (domain_names)
        status_dict = {}
        for d_name in domain_names:
            full_d_name = d_name+'.'+hostname_end
            try:
                whois_info = whois.whois(full_d_name)
                if whois_info['status'] == None:
                    status_dict[full_d_name] = "Avaliable"
                else:
                    if type(whois_info['expiration_date']) is list:                 
                        status_dict[full_d_name] = whois_info['expiration_date'][0]
                    else:             
                        status_dict[full_d_name] = whois_info['expiration_date']

            except whois.parser.PywhoisError:
                status_dict[full_d_name] = "Avaliable"
            
        return status_dict
    def Dump_To(self,file,domains_status):
        with open(file,'w+') as f:
            for key,value in domains_status.items():
                f.write(key+' - '+str(value)+'\n')
            f.truncate()
            f.close()
        




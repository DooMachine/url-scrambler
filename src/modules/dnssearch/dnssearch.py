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
                    status_dict[full_d_name] = "Not Avaliable"
            except whois.parser.PywhoisError:
                status_dict[full_d_name] = "Not Avaliable"
            
        return status_dict
    def Dump_To(self,file,domains_status):
        with open(file,'w+') as f:
            for key,value in domains_status.items():
                f.write(key+' - '+value+'\n')
            f.truncate()
            f.close()
        




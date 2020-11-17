import os
import time
import json
import requests
import subprocess




def parseAmazon(offerListingID,asin,merchantID):
    os.system('curl.exe  "https://www.amazon.com/gp/product/handle-buy-box/ref=dp_start-bbf_1_glance"   -H "authority: www.amazon.com"   -H "cache-control: max-age=0"   -H "rtt: 100"   -H "downlink: 9.8"   -H "ect: 4g"   -H "upgrade-insecure-requests: 1"   -H "origin: https://www.amazon.com"   -H "content-type: application/x-www-form-urlencoded"   -H "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"   -H "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"   -H "sec-fetch-site: same-origin"   -H "sec-fetch-mode: navigate"   -H "sec-fetch-user: ?1"   -H "sec-fetch-dest: document"   -H "referer: https://www.amazon.com/dp/B077R2F5BT/ref=sspa_dk_detail_2?psc=1&pd_rd_i=B077R2F5BT&pd_rd_w=94BvG&pf_rd_p=f0355a48-7e73-489a-9590-564e12837b93&pd_rd_wg=PVrzI&pf_rd_r=W7PZB872P9ABYA6MVDX2&pd_rd_r=b97cfb90-e4b4-4a10-94f1-75bd5eb118d4&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyOFJUU1hOUzNXSFc3JmVuY3J5cHRlZElkPUEwNDcwNzU3MUQxWDU4Vk1NMVo1VyZlbmNyeXB0ZWRBZElkPUEwMTc4OTM3Qk1TQTVOR1VCVzkyJndpZGdldE5hbWU9c3BfZGV0YWlsX3RoZW1hdGljJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="   -H "accept-language: en-US,en;q=0.9,es;q=0.8"   -H "cookie: session-id=135-7153861-6337254; ubid-main=134-1312144-2847069; _mkto_trk=id:365-EFI-026&token:_mch-amazon.com-1603410169314-18926; x-main="@tPFmFlVDiqIRn5@D@zUHMROzAWOSwiCITSLZgecmXxL26FLIs30lDELFkJfh06a"; at-main=Atza|IwEBIPoC7C7c7TpbzojsWt43zDy7BlV3PyRWAKBp00jf1H3up6F-9KgLO4KnHlZX0fkXFvcojjmXvks7RR71aV87_VElE5HCnWaTIcBP-iNyjf-ut-DHkOaRt9HaGka8HCLFxFSfYnXTuEtI-XRo5KXQ0oCkkgZnGrneJwFraf65snskSOTBAxZGx6EC706QwaV78mKgTx9wrhIAgat6UELPPDoQ; sess-at-main="k1JnShxxF/Uy3WUhVwKySTiKDdlS+NJ/OQEmXYCIlRs="; sst-main=Sst1|PQEguUN2qA1xZdWR21W9u1UKCV0tCBCGHbRB23SbC1jeTkOaRfc7nvqRtwwnnNmz3buhvuTSWxKanSJs4RHwmm_mhq76ncpUX5_2w7nq_s5R3pctC-xfz2ZADsyPVloC_pZslcGp60EUSpbs1WcBMPEbfOW6-D0wqm_oMW9wa3MzIrVliMCp9Jdb58S97hynbyHvQ2-K6EOaFFdHdYQ9loPzvw9Oi3ncSzJ62PkKJCR-jJaFB0OP9Qt0fmN6rZ5NeWPHzvtiUqeqb80EnG6No5oc-AZUP7wxAs0rvFPsCowqxyI; session-id-time=2082787201l; i18n-prefs=USD; sp-cdn="L5Z9:PH"; lc-main=en_US; AMCV_4A8581745834114C0A495E2B%40AdobeOrg=-408604571%7CMCIDTS%7C18560%7CMCMID%7C65743519953523193858248051727005190133%7CMCAID%7CNONE%7CMCOPTOUT-1603516841s%7CNONE%7CvVersion%7C4.6.0; s_nr=1603509641572-Repeat; s_lv=1603509641573; skin=noskin; session-id-eu=258-1547120-6857261; ubid-acbuk=257-3890710-8149226; csm-hit=tb:MNBPD9W1KF5MY2AV3Z7R+s-431AK0N8AG5XQZEDWXBS|1603529966643&t:1603529966643&adb:adblk_no; session-token=+noJVXWTVndhnIxz6tfchVqUhv27KunxF1/yTF0C8GdtLbvrhXZ1cjQv3MYcvva0D4re8vzh2AWLd6nVtq4BOTT+V2kV27OUHd5WSPX9QTdq9U8McAN2/r0kU07CIiAI+8YxRZhxMmtBXFmsrkxxIsqOh+gxvVzyLLZxbcgQOzlThhaXZpsyCWebf0D1CQ4jh0favmA/SZHpkrp7wxaiAjVOqNKqNHMnPD+Zz+r9zamdst/0iTqju3lyoIXpiDEC71DFOw0oyb8Nxx9vQ9sQ8A=="   --data-raw "offerListingID='+offerListingID+'&session-id=135-7153861-6337254&ASIN='+asin+'&isMerchantExclusive=0&merchantID='+merchantID+'&nodeID=&sellingCustomerID=&qid=&sr=&storeID=&tagActionCode=&viewID=glance&rebateId=&ctaDeviceType=desktop&ctaPageType=detail&usePrimeHandler=0&rsid=135-7153861-6337254&sourceCustomerOrgListID=&sourceCustomerOrgListItemID=&wlPopCommand=&quantity=4530&submit.add-to-cart=Add+to+Cart&dropdown-selection=mikoroistlkq&dropdown-selection-ubb=mikoroistlkq" --compressed   -o asd.htm')
    return ""


def parseInfo(asin):

    os.system('curl.exe "https://www.amazon.com/dp/'+asin+'" -H "authority: www.amazon.com" -H "cache-control: max-age=0" -H "rtt: 250" -H "downlink: 10" -H "ect: 4g" -H "upgrade-insecure-requests: 1" -H "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36" -H "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9" -H "sec-fetch-site: same-origin" -H "sec-fetch-mode: navigate" -H "sec-fetch-user: ?1" -H "sec-fetch-dest: document" -H "referer: https://www.amazon.com/" -H "accept-language: en-US,en;q=0.9,es;q=0.8" -H "cookie: session-id=135-7153861-6337254; ubid-main=134-1312144-2847069; _mkto_trk=id:365-EFI-026&token:_mch-amazon.com-1603410169314-18926; x-main="@tPFmFlVDiqIRn5@D@zUHMROzAWOSwiCITSLZgecmXxL26FLIs30lDELFkJfh06a"; at-main=Atza|IwEBIPoC7C7c7TpbzojsWt43zDy7BlV3PyRWAKBp00jf1H3up6F-9KgLO4KnHlZX0fkXFvcojjmXvks7RR71aV87_VElE5HCnWaTIcBP-iNyjf-ut-DHkOaRt9HaGka8HCLFxFSfYnXTuEtI-XRo5KXQ0oCkkgZnGrneJwFraf65snskSOTBAxZGx6EC706QwaV78mKgTx9wrhIAgat6UELPPDoQ; sess-at-main="k1JnShxxF/Uy3WUhVwKySTiKDdlS+NJ/OQEmXYCIlRs="; sst-main=Sst1|PQEguUN2qA1xZdWR21W9u1UKCV0tCBCGHbRB23SbC1jeTkOaRfc7nvqRtwwnnNmz3buhvuTSWxKanSJs4RHwmm_mhq76ncpUX5_2w7nq_s5R3pctC-xfz2ZADsyPVloC_pZslcGp60EUSpbs1WcBMPEbfOW6-D0wqm_oMW9wa3MzIrVliMCp9Jdb58S97hynbyHvQ2-K6EOaFFdHdYQ9loPzvw9Oi3ncSzJ62PkKJCR-jJaFB0OP9Qt0fmN6rZ5NeWPHzvtiUqeqb80EnG6No5oc-AZUP7wxAs0rvFPsCowqxyI; session-id-time=2082787201l; i18n-prefs=USD; sp-cdn="L5Z9:PH"; lc-main=en_US; session-id-eu=258-1547120-6857261; ubid-acbuk=257-3890710-8149226; AMCV_4A8581745834114C0A495E2B%40AdobeOrg=-408604571%7CMCIDTS%7C18560%7CMCMID%7C65743519953523193858248051727005190133%7CMCAID%7CNONE%7CMCOPTOUT-1603543041s%7CNONE%7CvVersion%7C4.6.0; s_nr=1603535841484-Repeat; s_lv=1603535841485; session-token="dsHwL8+bZPFegC+JwcpD7wxZYEYEv8IgDb/DcSDf/v7hqTudeO5VwmRYSInbnzaB40aq215uCSjhKYR8z1yrVj5Obdl2tZeG9C7kIIgYUjLbUhVcKq3euFmURwPIHpvuj0QXev/1r5ffaX1CQM/DilYqCB6uPmR9x4gOKZ2g+kgQAxd/yQBFuoH2iYkA71wO7x/ufxSz0S3E88ljzcc0Wg=="; skin=noskin; csm-hit=tb:BDPTPHR39AEBJN97F81M+s-MXAKRQ7JRT9B3RYVTTKS|1603583605957&t:1603583605957&adb:adblk_no" --compressed -o result.txt')

    return ""



def getFees(asin,height,weight,length,width):

    cmd = "node 1.js "+str(height)+" "+str(weight)+" "+str(length)+" "+str(width)+" "+asin

    output = subprocess.check_output(cmd, shell=True)
    
    output = str(output).replace("\\n","").replace("'","")
    final = ""
    start = False
    for i in range(0,len(output)):
        if output[i]=='{':
            start = True
        if start==True:
            final += output[i]
    
  
    return final



def getInfos(contents):

   
    result = []
    values = ["offerListingID","ASIN","merchantID"]
   
    for value in values:
        try:
            tmp = 'name="'+value+'" value="'
            olipos = contents.index(tmp)+len(tmp)

            tmp1 = ""
            for i in range(olipos,len(contents)):
                tmp1 += contents[i]

                if contents[i+1]=='"':
                    result.append(tmp1)
                    tmp1 = ""
                    break
        except:
            print("NOT SEEN")
    

    price = ""



    cues = ['newBuyBoxPrice','price_inside_buybox"']

    for cue in cues:
        tmp2 = cue

        try:
            pspos = contents.index(tmp2)+len(tmp2)
            

            start= False
            for i in range(pspos,len(contents)):
                if contents[i]=='>':
                    start = True
                    i+=1
                if start==True:
                    price += contents[i]
                if start==True and contents[i+1]=='<':
                    break
                
            print(">>>>"+price)      
            price = price.replace("\n","")
            
            
        except:
            print("NOT THERE")

    
    result.append(price)



    tmp3 = "Best Sellers Rank"
    bsrpos = contents.index(tmp3)+len(tmp3)
    ranks = []
    product_image = ""

    start = False
    built = ""
    for i in range(bsrpos,len(contents)):
        if start==False and contents[i]=='<' and contents[i+1]=='s' and contents[i+2]=='p':
            start = True
            i+=  6
        if start==True:
            built += contents[i]
        
        if start==True and contents[i+1]=='<' and contents[i+3]=='s':
           
                ranks.append(remove_html_markup(built))
                built = ""
                start = False
                if len(ranks)>=2:
                    break

        

    img = 'id="landingImage" data-a-dynamic-image="{&quot;'

    imgPos = contents.index(img)+len(img)

    theimage = ""

    for i in range(imgPos,len(contents)):
        theimage += contents[i]
        if contents[i+1]=='&':
            break
    

    sname = 'id="bylineInfo"'

    snamePos = contents.index(sname)+len(sname)

    sellers_name = ""

    start = False
    for i in range(snamePos,len(contents)):
        if contents[i+1]==">":
            start = True
            i+=1
        if start==True:

            sellers_name += contents[i]

        if start==True and contents[i+1]=='<':
            sellers_name = sellers_name.replace("Visit the ","").replace(">>","")
            break
    



    result.append(ranks)
    result.append(theimage)
    result.append(sellers_name)


    return result



def remove_html_markup(s):
    tag = False
    quote = False
    out = ""

    for c in s:
            if c == '<' and not quote:
                tag = True
            elif c == '>' and not quote:
                tag = False
            elif (c == '"' or c == "'") and tag:
                quote = not quote
            elif not tag:
                out = out + c

    if "(See" in out:
        out = out.split("(")[0]

    return out.replace("\n","").replace("#span","").replace("span","")



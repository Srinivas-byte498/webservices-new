from metadata.functions.database import validateCookieDB,getMenuItemsByCustomerStatusDB, getProfileQuestionsDB,getLookUpID, getLookUpValues
import logging


def validateCookieService(request):
    try:
        if 'userName' in request.COOKIES:
            
            if validateCookieDB(request.COOKIES['userName']):
                return request.COOKIES['userName']
            else:
                raise Exception("Authentication failure")   
        else:
            raise Exception("Authentication failure")  
    except Exception as e:
        logging.error("Error in validating Cookie Service "+str(e))
        raise  

def getMenuItemsByCustomerStatuService(customerStatus):
    try:
        menuItemList= getMenuItemsByCustomerStatusDB(customerStatus)
        
        temp = []
        
        for menuItemObj in menuItemList:
           
            menuItemObjList = [menuItem for menuItem in temp if menuItem['menuItemParent'] == menuItemObj.menuItemParent]
            
            if len(menuItemObjList) == 0:
                    
                uiMenuItemObj = {
                    'menuItemParent':menuItemObj.menuItemParent,
                    'UIIcon': menuItemObj.UIIcon,
                    'menuItemKey':menuItemObj.menuItemKey,
                    'child':[] 
                }
                uiMenuItemObj['child'].append({'menuItemName':menuItemObj.menuItemName,'menuItemLink':menuItemObj.menuItemLink})
                temp.append(uiMenuItemObj)
            elif len(menuItemObjList) == 1:
                temp=[menuItem for menuItem in temp if menuItem['menuItemParent'] != menuItemObj.menuItemParent]   
                menuItemObjList[0]['child'].append({'menuItemName':menuItemObj.menuItemName,'menuItemLink':menuItemObj.menuItemLink})         
                temp.append(menuItemObjList[0])
        
        menuItemList = temp
        return menuItemList
    except Exception as e:
        logging.error("Error in retrieving menu items by customer status service" + str(e))
        raise


def getProfileQuestionsService(profqclass):
    try:
        profileQuestions=getProfileQuestionsDB(profqclass)
        
        temp = []
        
        for profileQuestion in profileQuestions:
           
            profileQuestionsObj = {
                'profqname':profileQuestion.profqname,
                'profqtype':profileQuestion.profqtype,
                'profqorder':profileQuestion.profqorder,
                'values':None
            }
            if profileQuestion.profqchoicelabels != "null":
                vals=profileQuestion.profqchoicelabels
                profilevalues=vals.split(",")
                profileQuestionsObj['values']=profilevalues
            temp.append(profileQuestionsObj)
        profileQuestions = temp
        profileQuestions = sorted(profileQuestions,key=lambda x:x['profqorder'])
        return profileQuestions
    except Exception as e:
        logging.error("Error in retrieving profile questions service "+str(e))
        raise

def getCountryCodesService():
    try:
        lookupValueObj =  getLookUpID('countryCode')
        masterLookupObjs = getLookUpValues(lookupValueObj[0].lookupid)
        countryCodeList = []
        for masterLookupObj in masterLookupObjs:
            obj = {
            'countryCodeValue':masterLookupObj.lookupname,
            'countryCodeDisplayVal':masterLookupObj.lookupparam1
            }
            countryCodeList.append(obj)
       
        return countryCodeList       
    except Exception as e:
        logging.error("Error is retreieving country codes service"+str(e))         
        raise
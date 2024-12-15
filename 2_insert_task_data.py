import sqlite3
from datetime import datetime

def connect_db(db_name):
    #file_path = 'D:/Users/ramammadov/Desktop/All_Python_Script/test_django/task_manager/db.sqlite3'
    conn = sqlite3.connect(db_name)
    return conn


# Function to delete all tasks from the 'tasks_task' table
def delete_all_tasks(conn):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM task")
    conn.commit()
    print("All tasks have been deleted.")


# Function to insert tasks from a list into the 'tasks_task' table
def insert_tasks_from_list(conn, tasks_data):
    cursor = conn.cursor()

    # Iterate over the list of task data and insert each task
    for task in tasks_data:
        title = task['title']
        description = task['description']
        created_at = task['created_at']
        status = task['status']
        completed_at = task.get('completed_at')  # It may be None
        completed_by_id = task.get('completed_by_id')  # It may be None

        cursor.execute(
            """
            INSERT INTO task (title, description, created_at, status, completed_at, completed_by_id)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (title, description, created_at, status, completed_at,
              completed_by_id))

    conn.commit()
    print(f"{len(tasks_data)} tasks have been inserted.")


# Function to display all tasks (optional, for verification)
def display_tasks(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM task")
    tasks = cursor.fetchall()

    print("Tasks in the database:")
    for task in tasks:
        print(
            f"ID: {task[0]}, Title: {task[1]}, Status: {task[4]}, Created At: {task[2]}, Completed At: {task[5]}, Completed By ID: {task[6]}"
        )


# Main function to execute the steps
def main():
    db_name = '/home/ramil/awesome_projects/test_diff/flask_task_manager/instance/tasks.db'
    #'D:/Users/ramammadov/Desktop/All_Python_Script/test_django/task_manager/db.sqlite3'
    
    #'db.sqlite3' #'tasks.db'  # SQLite database file name
    conn = connect_db(db_name)

    # Delete all existing tasks
    # delete_all_tasks(conn)

    # Define the list of task data to insert
    # List of titles and descriptions
    titles_and_descriptions = [
        #    ('Meeting with the marketing team', 'Discuss the upcoming marketing campaigns and budget allocations.'),
        #    ('Develop new feature for the app', 'Implement the user authentication feature for the app.')
        ('3C629F4A-BABC-4CEC-90EB-E14D66D1B824',
         'http://powerbi/reports/powerbi/BI/Strategy_Investment/Investment/USD_muracietleri'
         ),
        ('C45C41B1-0ADF-40AC-8083-187946B83FC6',
         'http://powerbi/reports/powerbi/BI/Sales_Marketing/Marketinq_mahsulun_inkishafi/hys_claim_muraicetler'
         ),
        ('43E22A4C-94D1-421F-9F74-A04639E99230',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Claims/Claim_app'
         ),
        ('41A14630-5372-455F-B17D-82B4568B2FE9',
         'http://powerbi/reports/powerbi/BI/Finance/Financial_Supervision/Debitor/Debitor RAS/CPA_KHS_debitor_borc'
         ),
        ('D08EB57F-594F-424B-AB45-B01E640330E5',
         'http://powerbi/reports/powerbi/BI/Finance/Financial_Supervision/CPA_KHS_debitor_borc'
         ),
        ('B49E16D5-0A87-439E-857B-78671AB79858',
         'http://powerbi/reports/powerbi/BI/Finance/Financial_Supervision/Debitor/CPA_KHS_debitor_for_sale'
         ),
        ('B39FADA3-BC5F-4885-85A9-E24E4C78FDA1',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/CPA_Yenilnmə'),
        ('F5C799E8-CA3C-4EE0-9881-33B5E8B6237E',
         'http://powerbi/reports/powerbi/BI/Other/CPA SQUAD REPORTS/All_Debitor_Contract_Or_Addition_Data_Table'
         ),
        ('A5096060-E4A9-46A8-9B0B-8D9F74F9DBB5',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/aktiv_icbari_sh_mxs'
         ),
        ('7CA922DA-7451-41E4-A107-D49544C743B5',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/Active_CPA_Employee_Count'
         ),
        ('632C864F-628D-4F89-A6BC-6B2AD92C0CD9',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/Aktiv_icbari_'
         ),
        ('1EA599AA-CF41-4C66-A2FD-C9C1B9657E9D',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/Icbari_Aktiv_melumatlari'
         ),
        ('99D567EF-D102-47C3-832E-469E1909248F',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/İcbari_Şirkət GWP'
         ),
        ('2E8B663F-1CD6-48A7-93F6-5062D02BA2F1',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/J-62_2018_GWP'),
        ('AFF62AEF-4C61-4665-BF87-3A3F66A90314',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/KHS_Yenileme'
         ),
        ('38CD9B48-9AEC-450F-9D84-7B0AA4C89806',
         'http://powerbi/reports/powerbi/BI/Other/4.cü rüb üzrə İcbari sığortaya yeni qoşulan müştərilər'
         ),
        ('3D82B641-3EB4-456C-ABA0-C3988B13EB54',
         'http://powerbi/reports/powerbi/BI/Other/Sanan/CPA_active_müştəri_email_rüb'
         ),
        ('24C533E9-F56A-41C5-AE0A-0F3C30784704',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/Icbari_polislerin_Statusu'
         ),
        ('922506C1-478C-4A9D-B8B8-17D0AE4866B9',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/PH_HYS_Bonus_Netice'
         ),
        ('CDA7162B-2C5D-4D4D-A649-F92567A7DF6D',
         'http://powerbi/reports/powerbi/BI/Other/Rüblər üzrə CPA'),
        ('1884123F-0EA4-4590-BA76-265BFE6E74AE',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Underwriting_Reinsurance/HYS_Company_Job'
         ),
        ('66C36349-CC98-47A1-B886-200ADE0BCD3E',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/CPA_Yenilnme'),
        ('C47D3B4D-39FE-4994-9125-0B0B967C4472',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/CPA_ReNew'),
        ('3F2FB3BA-5228-4E3C-A28D-6C56EF6167BF',
         'http://powerbi/reports/powerbi/BI/Sales_Marketing/Banks/Banklar_uzre_neticeler'
         ),
        ('FA1BAEC8-BF3D-4E81-A7EB-4D20D8E8C9C0',
         'http://powerbi/reports/powerbi/BI/Other/HYS_Faydalanan'),
        ('BCDD2E12-3731-4741-A25F-9488CF7AEC0B',
         'http://powerbi/reports/powerbi/BI/Other/Icbari_faydalanan'),
        ('9DA8C685-9011-4C30-BE7A-045BF6D81DEA',
         'http://powerbi/reports/powerbi/BI/Other/Icbari_faydalanan_V2'),
        ('8CCF4349-AD95-461C-8F8B-6750D7524D11',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Claims/Arxiv/HYS_Claim_raport(kohne)'
         ),
        ('EA88DE44-B037-4A64-9CA3-F37CD38B6B18',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/Qanunvericikle_baglı_Kutlevi_azalma_Hesabati_General'
         ),
        ('BF0B95CE-3203-4F79-9BB9-8C2BA520C23B',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/Qanunvericikle_baglı_Kutlevi_azalma_Hesabati_Detailed'
         ),
        ('80D9A2EA-BB33-42CE-AE21-71D5087091B0',
         'http://powerbi/reports/powerbi/BI/Finance/Accounting/KHS_Register'),
        ('D2E60CB7-FC37-479E-ABF0-64930A723BD7',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Support_to_Insurance_Operations/Veybl'
         ),
        ('57354F50-C7E5-4AA9-A46F-51FD8764322E',
         'http://powerbi/reports/powerbi/BI/Other/Neqliyyat_istifadesi'),
        ('B27DD1FF-54F7-479D-8C3F-7A3EADB597DC',
         'http://powerbi/reports/powerbi/BI/Other/CPA SQUAD REPORTS/CPA_Xitam_Sebebler'
         ),
        ('54C44276-BCF9-4763-BEC3-5439A09F41C7',
         'http://powerbi/reports/powerbi/BI/Other/CPA SQUAD REPORTS/CPA_YENİ_YENİLENME_KPİ'
         ),
        ('5D748938-FF93-4A36-9B34-B5A60AA1D401',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/ISB'
         ),
        ('62E90244-393B-4525-ACCA-82EC698ED512',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Operational_Risks_Management/cpa_mno_voen'
         ),
        ('0DF4B3F5-6C62-45BC-9013-A85E47BE5B75',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/CPA_Yenilənməyənlər'
         ),
        ('991D995B-1E82-41B0-BE36-CC43AEA351F7',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/Icbari_hissevi'),
        ('EFBCE006-61BE-4631-89A7-85C3ED09B6AB',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/Icbari_Hissevi_odenishler'
         ),
        ('6207288B-B40F-44AC-BBD1-142A4CB4E706',
         'http://powerbi/reports/powerbi/BI/Other/CPA SQUAD REPORTS/CPA_Budge_Control'
         ),
        ('B19E741D-E42C-4B94-ABE3-FA83F8DAEBB3',
         'http://powerbi/reports/powerbi/BI/Other/CPA SQUAD REPORTS/Strateji_Company_List'
         ),
        ('EA9BE40B-2AF1-491D-9DB8-563192CAAA70',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/CPA_New_Gwp'),
        ('5BC348F2-8436-4EFD-8B06-563FEF795A64',
         'http://powerbi/reports/powerbi/BI/Finance/Accounting/HYS_REGISTR(2)'
         ),
        ('A8366946-26A7-48C4-8919-76775F8B7079',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Operational_Risks_Management/GHS_aktiv_faydalalan'
         ),
        ('E7228685-65E1-4FE4-AA38-A8AF6C1D97B7',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Underwriting_Reinsurance/Group_risk_inf'
         ),
        ('16F0F74C-B2A6-4224-9055-2D6DF2534376',
         'http://powerbi/reports/powerbi/BI/Independent departments/Internal Audit Servis/ƏLAQƏLƏRİN BƏYAN EDİLMƏSİ FORMASI'
         ),
        ('0373FCBB-B3BB-41D5-98FD-3C424597A719',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Support_to_Insurance_Operations/Operation_Duration'
         ),
        ('17DFFB4B-87B0-4EA4-BA9E-FCEACCB10FE7',
         'http://powerbi/reports/powerbi/BI/CBAR/Aidiyyati_shexsler_uzre_aktiv_muqavileler'
         ),
        ('4E9E4ED1-6CDE-4760-A6B5-ED5B7B487642',
         'http://powerbi/reports/powerbi/BI/Other/Audit_xitam_legv_mehsullar'),
        ('70B11C5A-0176-4FDA-B593-175DBE064658',
         'http://powerbi/reports/powerbi/BI/Other/Claim_mno_sm'),
        ('C09762D0-20AB-4F24-B635-C90191506B16',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Support_to_Insurance_Operations/Sened_Sayi'
         ),
        ('C0D3B17E-3E02-4C70-B4C4-2841623EC8CB',
         'http://powerbi/reports/powerbi/BI/Strategy_Investment/Investment/Konvertarsiya_muracietleri_yeni_sistem'
         ),
        ('21C3172D-F54D-4931-A29C-5D3FB994F5DE',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Pricing_Portfolio_Analysis/HYS_data'
         ),
        ('04B233A7-B3A2-4F1B-BB21-B1FC38AC9CCF',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Pricing_Portfolio_Analysis/HYS_data_test_with_duration'
         ),
        ('9733FD71-DEB0-45BB-BD0F-FCE58CC2539E',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Pricing_Portfolio_Analysis/HYS_data_with_dates'
         ),
        ('F95992A8-8235-499C-BA7D-34709A52EBAB',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Pricing_Portfolio_Analysis/HYS_Raport_2'
         ),
        ('32E403B1-5718-4740-9343-F12B7C267F32',
         'http://powerbi/reports/powerbi/BI/Other/Legal_Support/HYS_GHS_FOR_FATCA_CRS'
         ),
        ('491EE8AB-016C-4541-8D1F-2FBCBEF07741',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Insurance_Risks_Reserving/yeni_icbari_register'
         ),
        ('4594B527-526D-4ABD-82C1-D1EA8772034C',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/IFRS/Cpa_For_Ifrs'
         ),
        ('C247EA5B-02BE-4720-A1AD-24FBC5909BEF',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/IFRS/KHS_For_IFRS'
         ),
        ('2A1FD32E-EDF8-4C75-BDDC-08E14C6C6F23',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Pricing_Portfolio_Analysis/Arxiv/Mli_Registr'
         ),
        ('37433D14-89DE-4A56-9213-B78725ED0E66',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/Raports_Pincode'
         ),
        ('3EA4F62E-0020-4174-9440-37B4CA49F597',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Insurance_Risks_Reserving/Risk_Jurnal_Muqavileler'
         ),
        ('1FBFF34F-1070-4D51-8624-432D1AE550B6',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Pricing_Portfolio_Analysis/CB_Register'
         ),
        ('F8178644-63E2-43FD-861B-1544316FC4E7',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Pricing_Portfolio_Analysis/GHS_Register'
         ),
        ('171D1EA9-0F89-4F82-8709-AF31E7BB9A61',
         'http://powerbi/reports/powerbi/BI/Finance/Accounting/GHS_Register'),
        ('26AA7288-EEF0-4A80-98B9-D6FFCB0E66C0',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/Aktiv Fin'),
        ('813483A9-9D20-450E-862E-A54D4C4A651F',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/GHS_yenileme'),
        ('CD60F2EC-906C-405F-9111-B81C404FD1EB',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Insurance_Risks_Reserving/Məhsullar Bütün Sütunlar/Icbari_Butun_Statuslar'
         ),
        ('8C071047-330F-432F-B588-DD7A3E20BC7B',
         'http://powerbi/reports/powerbi/BI/Strategy_Investment/Strategy_Research/HYS_Customer'
         ),
        ('39029669-0C4C-46E9-8D4E-4AC47769E810',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Pricing_Portfolio_Analysis/FHS_Muqavile_Teminat'
         ),
        ('26B20D1D-DBAE-474A-8AC3-CEDA264474D1',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Pricing_Portfolio_Analysis/HYS_APG_FHS_Risk_Meblegi'
         ),
        ('A8B5EC03-3C81-49A9-A2E3-53F21AF4C4FB',
         'http://powerbi/reports/powerbi/BI/Other/HYS_uzre_melumatlar'),
        ('8820FC8D-5B39-4BC6-9B06-D84A1B9FCC6B',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/Gelirliyi_Azalan_HYS'
         ),
        ('63B02E18-243B-48AE-A09F-687C7E007A68',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/Gelirliyi_Azalmayan_HYS'
         ),
        ('BBA6731A-42AB-4888-84F1-B9B512342A84',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Underwriting_Reinsurance/HYS_BH_RM'
         ),
        ('BEE5FB15-1CB5-41E8-BE7F-67CBF5FC0A9A',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/HYS data_For_Sales'
         ),
        ('57A40A04-C080-494A-AAD9-9DCCB3B3C889',
         'http://powerbi/reports/powerbi/bi/hr/Incentive/HYS_Müqavilə'),
        ('26CFD942-3C92-4C48-AD0C-A9E2DAFBF29B',
         'http://powerbi/reports/powerbi/BI/test/HYS_Müqavilə_Bonus'),
        ('35A219E5-ED7E-45CB-9355-9730D735C083',
         'http://powerbi/reports/powerbi/bi/hr/Incentive/HYS_Bonus/HYS_Müqavilə_Bonus_2021'
         ),
        ('39D77D36-CF80-4E27-811E-676B9BE2F2CE',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/NSSP/Strategiya_GHS_Yeni_Kohne_Musteri'
         ),
        ('5EAFD587-9AE3-4592-8CF0-FCD11B38660D',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/Asan_imza'
         ),
        ('00838649-0FE2-428F-9436-F2C119BCD2BD',
         'http://powerbi/reports/powerbi/BI/Other/Legal_Support/HYS_GHS_sened'
         ),
        ('2AB21C23-70CD-4F2D-953C-EEF71AEBE93F',
         'http://powerbi/reports/powerbi/BI/IT/Pin'),
        ('74ED0BB7-F8F9-4DD5-AADF-8351398989FC',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/NSSP/GHS_report_musteri_tipi'
         ),
        ('517630FB-9283-4BFF-954C-216E6DCC5DB6',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/NSSP/GHS_report_musteri_tipi_V3'
         ),
        ('57D85FFD-48F3-44A4-835D-9C664CACD5EC',
         'http://powerbi/reports/powerbi/BI/Strategy_Investment/Strategy_Research/HYS_Gelecek_ay'
         ),
        ('341C4D0A-5663-4257-B3CB-92DE82425C56',
         'http://powerbi/reports/powerbi/BI/Sales/z_Arxiv/HYS_Gelecek_ay (2)'),
        ('3C019D06-785F-4486-9CCD-F46259990111',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/HYS_Gelecek_ay_Xitam_daxil'
         ),
        ('D7BA6575-9260-4C3B-95B8-A607894B6521',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/HYS_Gelecek_ay_Xitam_daxil_2022'
         ),
        ('DAAE60DD-55E6-42E1-A352-0BE2D22FF2D7',
         'http://powerbi/reports/powerbi/BI/Strategy_Investment/Strategy_Research/Active_Client'
         ),
        ('8F572729-F742-4FD1-9DA8-4D876F468DE7',
         'http://powerbi/reports/powerbi/BI/Strategy_Investment/Strategy_Research/Active_HYS_Client'
         ),
        ('797F095B-A190-4774-B809-DCFDA0B5D6D2',
         'http://powerbi/reports/powerbi/BI/Other/Active_mno'),
        ('92DDA905-3AB0-4B17-97A7-B150B7216BB8',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Underwriting_Reinsurance/Aktiv_HYS_mugavileler'
         ),
        ('3BF177F5-E91F-48C1-870B-FAF4B21C25D7',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/Aktiv_mugavileler_Freeze_daxil'
         ),
        ('E51545E5-444B-4173-914E-7ECC35215C91',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/bir_den_cox_mehsulu_olan'
         ),
        ('ACC0C661-C0C8-4805-9F0C-1919726E2761',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Call_Centre/Claim_GWP_detailed'
         ),
        ('FED1F53F-9FF7-4ABD-AB55-130203E5266D',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Call_Centre/Claim_Gwp_general'
         ),
        ('8FF575F7-EEB6-4358-B5F3-589C50BC71E5',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/DataIKU_UC_Result'
         ),
        ('EB3FAEEB-7DEE-43B4-849F-D2D5D90F1768',
         'http://powerbi/reports/powerbi/BI/Other/Legal_Support/Ending_contracts_HYS_GHS'
         ),
        ('D93E163F-BAF3-4583-B8B8-D19197E12C45',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/Fin_and_log_count'
         ),
        ('B480230B-10C4-4DD6-8741-F7AB54EC2788',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/For_Zakir_HYS'),
        ('118CBDD0-31B7-485D-8962-180199080A9C',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/For_Zakir_HYS_all_arxiv'
         ),
        ('4DB4DFA0-975F-4235-AB80-149420FC29AC',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/HYS_Cash_Flow'),
        ('6FCFFED2-5C43-4DCC-99FA-AB086D7988AA',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Insurance_Risks_Reserving/HYS_Claim'
         ),
        ('416B7043-2305-4A89-B37B-2B9C05DF4B8C',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/HYS_Cross_Sales'
         ),
        ('8A0FB309-C7D9-44AD-91D9-8793A6B140E7',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/hys_data_sh'),
        ('C9F0E7F3-8C9F-4583-96FA-47983B1A7FA8',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/HYS_Gwp'),
        ('5EAE1D93-54D4-41BF-B4FF-CD03BC5A9CE6',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/HYS_GWP_tarix_araligi'
         ),
        ('FC17E8E6-722D-40BC-AA0C-A87ED75FD126',
         'http://powerbi/reports/powerbi/BI/Sales_Marketing/Marketinq_mahsulun_inkishafi/HYS_ilk_mugavile_kanali'
         ),
        ('695987FE-51B0-4426-8463-13F443153400',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Pricing_Portfolio_Analysis/hys_kredit_info_for_pricing_'
         ),
        ('EF84B4C3-474C-40C0-A3BA-292207F4A9EB',
         'http://powerbi/reports/powerbi/BI/Finance/Financial_Supervision/HYS_mugavile'
         ),
        ('3DC3EAB9-B52D-412E-9AEF-2C0926FC4B69',
         'http://powerbi/reports/powerbi/BI/Independent departments/Internal Audit Servis/hys_old'
         ),
        ('A3CEC2EA-A404-4195-AC4D-BAE3DFB1BB5B',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/HYS_Paid'),
        ('A9D3908A-0CC1-4D78-AEE4-9425D66E42D2',
         'http://powerbi/reports/powerbi/BI/Strategy_Investment/Strategy_Research/HYS_pin_Max_SH_bonussuz'
         ),
        ('4B71BF57-B4B8-4A5C-85B6-A968819D9FC4',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/HYS_Retention_Sales'
         ),
        ('E5035E9C-A398-4795-A871-8259DC14B841',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/HYS_scan_file(PINCODE)'
         ),
        ('B6741F18-90FE-4B09-BC0B-351BC9189811',
         'http://powerbi/reports/powerbi/BI/test/Fatima/HYS_SH_AKTIV_FREEZE_MUG'
         ),
        ('016B852C-3613-4EA2-ABA7-765AA6CD6870',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Claims/Arxiv/HYS_SM_SH'
         ),
        ('492D8500-6FD1-4BD9-9B71-2DC7796590B1',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/Ipoteka_yenileme'
         ),
        ('CB5C37F3-B4B9-4C59-B939-E54E9DEA9FBD',
         'http://powerbi/reports/powerbi/BI/Sales_Marketing/Banks/MLI_fin_mno'
         ),
        ('6D2F79BC-1034-481C-9C3D-72A17A49BD54',
         'http://powerbi/reports/powerbi/BI/Sales_Marketing/Banks/MLI_mno_fin'
         ),
        ('8D455858-6290-4D9A-A82B-8989C6B32FA1',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Claims/Nusxe_HYS'
         ),
        ('C7346C24-9BAC-4475-A435-668799A83F16',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Underwriting_Reinsurance/TS_mugavile_ucun_aktiv_konullu_portfel'
         ),
        ('295F857C-4928-405F-BE5C-8C4AE01BF4EB',
         'http://powerbi/reports/powerbi/BI/Other/Legal_Support/Online payments'
         ),
        ('203B37A7-AC73-476E-9B99-4D76401B1EAA',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/MLI_FHS_APG_BOX_tel_nom'
         ),
        ('544CF0DB-6531-4BF3-BB46-BE6591866ACE',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Operational_Risks_Management/Lost_Client'
         ),
        ('EC73D887-6C08-498C-9308-6E02A46624F1',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Operational_Risks_Management/Lost_ClientV1'
         ),
        ('A6FFFAFF-E6DE-4433-B3B2-B98BAE0FE593',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Insurance_Risks_Reserving/Ucot_jurnali/cpa_changed_v2'
         ),
        ('DEAECD98-CF6D-49B3-AC88-A5D7D8CAA0FA',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Insurance_Risks_Reserving/CPA_For_Jurnal_Chaneged'
         ),
        ('EF2EF35F-4D20-47C8-AFE5-5222A36CD66E',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Insurance_Risks_Reserving/Ucot_jurnali/New_Included/CPA_For_Jurnal_New_Included'
         ),
        ('D2A6D5AB-8FB8-45EF-A7B3-89FCF29BFEAF',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Insurance_Risks_Reserving/Ucot_jurnali/New_Included/CPA_For_Jurnal_New_Included_crt_date'
         ),
        ('AEF844BD-FDA5-462F-B973-DED41424F924',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Insurance_Risks_Reserving/Ucot_jurnali/cpa_new_included_v2'
         ),
        ('534891F1-EB66-48CE-8DF4-81D03F1FC6C4',
         'http://powerbi/reports/powerbi/BI/test/given_pin_information'),
        ('B0822CE5-4D5B-4931-9088-48203B5C4FA1',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Insurance_Risks_Reserving/HYS_RE_SM'
         ),
        ('DDF04C71-ED92-4E8F-B1F3-7A330B785CEC',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/HYS_Xitam_For_Sales'
         ),
        ('04F63CD6-A244-45D2-B938-E24A71B9228B',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Insurance_Risks_Reserving/Ucot_jurnali/KHS_changed_menfi_sh'
         ),
        ('651BC667-144D-4A24-9262-9B1ABAC15AAC',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Insurance_Risks_Reserving/Ucot_jurnali/KHS_changed_menfi_sh_for_isb'
         ),
        ('D9392278-E6B1-4265-812E-12E4E2A04DC4',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Insurance_Risks_Reserving/Ucot_jurnali/KHS_new_included_menfi_sh'
         ),
        ('5154961A-9505-4DCE-87B3-9D2E8B716C69',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Insurance_Risks_Reserving/Ucot_jurnali/KHS_new_included_menfi_sh_for_isb'
         ),
        ('0E560286-B157-4FC7-B2F7-DCDCD002646F',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Operational_Risks_Management/Lost_client_v02'
         ),
        ('EB69EB45-B2EF-48ED-955F-350C6FF23317',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/Products_Count'
         ),
        ('C1E24E5E-E6E3-4DB7-9D8E-9C7E089B544C',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Insurance_Risks_Reserving/Ucot_jurnali/Changed/Ucot_jurnali_changed_CPA_KHS'
         ),
        ('876944ED-0A17-41C1-B875-5BD910FFD02A',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Insurance_Risks_Reserving/Ucot_jurnali/Changed/Ucot_jurnali_changed_CPA_KHS_crt_date'
         ),
        ('BC943038-9D80-46E8-8767-63F40B2E5521',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Insurance_Risks_Reserving/Ucot_jurnali/New_Included/Ucot_jurnali_KHS_new_included'
         ),
        ('FCF6C113-D21F-42F8-85E2-328597B878E2',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Insurance_Risks_Reserving/Ucot_jurnali/New_Included/Ucot_jurnali_KHS_new_included_crt_date'
         ),
        ('A6E74D87-4EF4-40CD-B8EB-954C10322F6F',
         'http://powerbi/reports/powerbi/BI/Agile/HYS/LMS clean leads'),
        ('DEE7748F-C3AF-4E59-B556-E009AAF9C9DE',
         'http://powerbi/reports/powerbi/BI/Agile/HYS/Bonus tracking - VIP'),
        ('930704D8-4392-4EF8-8B8D-0D4AEBD63487',
         'http://powerbi/reports/powerbi/BI/Agile/HYS/Bonus tracking'),
        ('A51E3FC0-C0E3-4215-B5A8-8797B5A825BB',
         'http://powerbi/reports/powerbi/BI/Agile/HYS/Bonus tracking - Comp'),
        ('DFE7FEFF-0CC9-49A5-81F4-420F7F4DF4FE',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/GWP_individual_Tarix_araligi'
         ),
        ('70E2F3B9-0C75-42F8-BBB9-8256C38F7748',
         'http://powerbi/reports/powerbi/BI/Other/Refinitiv_'),
        ('C3C42F65-5661-464C-B5A2-6178959DB3F7',
         'http://powerbi/reports/powerbi/BI/HR/Cancelation_date'),
        ('ACD2740F-B322-4AAE-9C14-D7FF1969C046',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/K2/K2_HYS'),
        ('78B6BABC-FF3A-4522-9796-5447F84D2642',
         'http://powerbi/reports/powerbi/bi/hr/Incentive/HYS_yeni_müştəri'),
        ('DC00713A-D60C-4176-8EC0-E495691D1A53',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/K2_Model'),
        ('95516D64-2792-44BF-BAF6-0301570D872E',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/compulsory_contract_ending_Date'
         ),
        ('061BB97B-1A4F-47D6-92B8-C3E5689439C4',
         'http://powerbi/reports/powerbi/BI/Agile/HYS/TEQ kompaniya results'),
        ('A8FCA6C7-C8BA-4474-B2E0-677D54AF42C5',
         'http://powerbi/reports/powerbi/BI/Other/CPA SQUAD REPORTS/CPA_SQUAD_XITAMA_GEDEN_MUQ'
         ),
        ('12E5FA42-8068-4F3A-82B9-9A68B0198FDA',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/HYS_Freeze'),
        ('08C33523-ABED-4DF1-B582-F8C90DE3CABA',
         'http://powerbi/reports/powerbi/BI/Other/Debitor_sms'),
        ('DA3BA5E2-9FF2-4C41-9193-FB7E22A160C2',
         'http://powerbi/reports/powerbi/BI/Strategy_Investment/Strategy_Research/HYS_GWP'
         ),
        ('FC800081-6224-4A67-AC9D-32B72EF3E822',
         'http://powerbi/reports/powerbi/BI/Strategy_Investment/Strategy_Research/HYS_GWP_TABLE'
         ),
        ('12937C83-12B4-453F-BCDD-E581B3C4533A',
         'http://powerbi/reports/powerbi/BI/HR/Vacation_list'),
        ('EF77AA82-05DB-447D-9D1C-1E17B9E35D02',
         'http://powerbi/reports/powerbi/BI/Other/CPA SQUAD REPORTS/AllDebitorContractOrAdditionTempTable_Last_Time'
         ),
        ('0C3ED162-945C-4818-A0B2-9EB6008727FD',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Underwriting_Reinsurance/TS_Bordero'
         ),
        ('928C587C-FE90-45CC-A048-6676C60CD439',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/Debitor_Report_All'
         ),
        ('A1964CB9-4853-498A-B99B-BC2BD9A5BC86',
         'http://powerbi/reports/powerbi/BI/Other/CPA SQUAD REPORTS/Debitor_All_Kohne'
         ),
        ('0452EBD5-89B7-442F-8833-3C2EB77CE8EB',
         'http://powerbi/reports/powerbi/BI/Other/CPA SQUAD REPORTS/Debitor_All'
         ),
        ('6871EA6A-7DE6-40E5-859A-ABB08FF1AA31',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/Cpa_mxsh_kurator'
         ),
        ('50866633-B782-4A99-A8B4-433F89C6053D',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/HYS_Mugavile_qoshulma_melumatlari'
         ),
        ('156AB655-381A-4397-8DBF-5E7886BC1EA1',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/CPA_Debitor_Target'
         ),
        ('94D95BA3-0E63-430C-8CF8-322AED7C79D2',
         'http://powerbi/reports/powerbi/BI/Finance/Accounting/Debitor_Accounting'
         ),
        ('63A8A055-8352-4289-8098-FA62921E6E61',
         'http://powerbi/reports/powerbi/BI/Finance/Accounting/hys_claim_faydalanan'
         ),
        ('66D23340-CB33-4647-8D19-6CC454A01C68',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/Icbari_senedler'
         ),
        ('369B7A43-5863-4396-B23B-D5F4997A0255',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/HYS_Lead_Bolgu'),
        ('DE134962-B6BA-4B72-9A8B-BBDAF0D10F57',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Pricing_Portfolio_Analysis/icbati_retention_data'
         ),
        ('62488ED0-C9C6-4EE5-A875-846FFE5EF47D',
         'http://powerbi/reports/powerbi/BI/Finance/Accounting/Icbari_Isci'),
        ('42114E3C-89E3-4824-A0DB-580B29FD724C',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Underwriting_Reinsurance/MLI_Hərbiçi_Günlük'
         ),
        ('04E573FA-FA19-47ED-BABD-2DD07103A93F',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Underwriting_Reinsurance/MLI_Hərbiçi_Ümumi'
         ),
        ('841DB371-1DB9-4EC5-B4E1-EAE54C4031B1',
         'http://powerbi/reports/powerbi/BI/Finance/Accounting/LMS_Report_'),
        ('A38BB1A5-06C5-452D-B6CA-5A5B3BB0A4EF',
         'http://powerbi/reports/powerbi/BI/Independent departments/Internal Audit Servis/Documents_Detailed'
         ),
        ('657BCF9A-FFED-423A-99E0-865F903E55DA',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Support_to_Insurance_Operations/İmzalanacaq senedin gonderilmesi'
         ),
        ('BA5BD971-4BE4-4459-AF73-BCC2BC56FB69',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Support_to_Insurance_Operations/Senedlerin imzaya gonderilmesi'
         ),
        ('707D16A2-F576-44FD-AA63-9D0024199451',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/New_Customer_Count_2'
         ),
        ('61EC44C7-7F2B-42C3-8C4D-5B2A44AE3C4C',
         'http://powerbi/reports/powerbi/BI/Other/Legal_Support/Active_GHS'),
        ('C7F1B0FC-5026-46DE-87EE-EE94172E0565',
         'http://powerbi/reports/powerbi/BI/Other/Legal_Support/Active_HYS'),
        ('6AEC3F79-83BD-41C5-A709-224FE08CBBA9',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Underwriting_Reinsurance/MLI_Herbici'
         ),
        ('3447611C-B61C-40CF-8D92-D0A70620FE8C',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/HYS_Telesales_BH'
         ),
        ('086FF601-2601-4513-9CAB-1C65DFBC469B',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Underwriting_Reinsurance/Ind._risk_inf'
         ),
        ('0A934CDC-E117-442B-9A32-7C4FC6AFB84B',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Underwriting_Reinsurance/Konullu_Detalli'
         ),
        ('B1CF54F5-D10D-4ACB-A528-6595103513AA',
         'http://powerbi/reports/powerbi/BI/Sales_Marketing/Marketinq_mahsulun_inkishafi/Kampaniya'
         ),
        ('A2D7A50A-A7C1-43A8-9D48-E1C9776BB541',
         'http://powerbi/reports/powerbi/BI/Agile/HYS/CRS_FATCA'),
        ('45895905-024A-4230-AB53-3C577ACB6C4E',
         'http://powerbi/reports/powerbi/BI/Finance/Accounting/mli_hadise_akt_siyahi'
         ),
        ('D67CF627-CC2C-4E7B-89FB-D460A1237B79',
         'http://powerbi/reports/powerbi/BI/test/MLi_comprehensive_solution'),
        ('E71DB79D-AB08-40E8-A0C7-C2E99577CB6B',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Claims/MLI_Kapital_Ipoteka_Fond'
         ),
        ('9D779564-2B08-42A1-BBD6-71DDD2D386B0',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Claims/Arxiv/MLIClaim'
         ),
        ('1320FAEA-827D-491E-B0E2-7D814CB39EC3',
         'http://powerbi/reports/powerbi/BI/Other/Claim_Data'),
        ('25ECBB2A-10BD-4C17-A0CE-C6698E96FEC2',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Insurance_Risks_Reserving/Ocr'
         ),
        ('51A0617D-6ABA-45A9-8805-7001AB6417E3',
         'http://powerbi/reports/powerbi/BI/Other/OCR_CPA'),
        ('EDAD2A7B-E486-47E3-B509-A7F81907DA1C',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Pricing_Portfolio_Analysis/OCR_CPA'
         ),
        ('EBCA3AB4-F164-44ED-9DE2-7E2F381D1B5B',
         'http://powerbi/reports/powerbi/BI/Other/Ocr_with_prd'),
        ('220E188D-96B6-4B32-BF34-83B1EFC448FF',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Claims/MLI_OCR'
         ),
        ('3D1D7EE9-49D4-4810-8E88-564D393F0A88',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Insurance_Risks_Reserving/GHS_Claim'
         ),
        ('B36D4FE8-DF9A-4E3F-823E-01AB8673B097',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Call_Centre/Claim_GWP_Issued_Detail'
         ),
        ('11F29EB4-DB3D-49D8-98E5-D6E58FDAB576',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Insurance_Risks_Reserving/HYS_Claims_report_OCR'
         ),
        ('B4457696-82EC-41D9-9D80-9E9C9123E302',
         'http://powerbi/reports/powerbi/BI/test/HYS_Claims_report_simplified'
         ),
        ('197D8898-EA6B-42A6-BFE5-DAAACFE1A6A6',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Claims/HYS_Claims_report_with_musteri_muracieti'
         ),
        ('0118D215-4692-4F06-AC53-26144C0E7F3B',
         'http://powerbi/reports/powerbi/BI/Finance/Accounting/HYS  claim registr(faydalanan2)'
         ),
        ('0F163A3D-3CF8-4AE9-803A-AB58BF465993',
         'http://powerbi/reports/powerbi/BI/test/MLI report st and qst status'
         ),
        ('B99B32AD-D349-477B-95A9-F06865169E3E',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Pricing_Portfolio_Analysis/MLI_Report_Muqavile_diger_teminat'
         ),
        ('7352F459-62A6-4E21-897D-3578C38F5AB2',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Pricing_Portfolio_Analysis/Arxiv/MLI_Regstr'
         ),
        ('B2BD9DCB-2800-4D59-94ED-E095221A3F65',
         'http://powerbi/reports/powerbi/BI/IT/One_time_downloaded/MLI_Report_Muqavile_2017'
         ),
        ('3F1EE514-AF43-49E0-BA4D-ABB0BBE8F0D1',
         'http://powerbi/reports/powerbi/BI/IT/One_time_downloaded/MLI_Report_Muqavile_2018'
         ),
        ('4432347F-F2FD-4CDA-A809-C58E1CCADF5C',
         'http://powerbi/reports/powerbi/BI/Sales_Marketing/Banks/Bank_aktiv_portfel'
         ),
        ('69BD1E93-AEAB-4820-8696-ABE379765731',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Pricing_Portfolio_Analysis/Arxiv/MLI_Report'
         ),
        ('35B83E94-8519-4675-8658-B72559A30E50',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Pricing_Portfolio_Analysis/MLI_Report_Muqavile_2011_2014'
         ),
        ('B2E013F4-286B-4419-AA5F-D65802B1E27B',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Underwriting_Reinsurance/MLI_Report_Muqavile_Pin'
         ),
        ('54B7CF22-6E48-4B60-8DAA-AE1B3337A5E6',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Pricing_Portfolio_Analysis/MLI_Restrukturizasiya'
         ),
        ('B15DEC6D-FF9F-4691-97A9-79CFD4F06366',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Pricing_Portfolio_Analysis/Arxiv/MLI_Report_Cutten_Arxiv'
         ),
        ('0333C463-D4E0-493D-A6DD-7A72821F7DF2',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Pricing_Portfolio_Analysis/Arxiv/MLI_Report_muqavile_Arxiv'
         ),
        ('A2E7058A-7BCB-4A9E-B138-C4A327A517DF',
         'http://powerbi/reports/powerbi/BI/Other/Legal_Support/GHS_xitam'),
        ('8EE89168-AD16-452F-B8B7-D6543EC3307C',
         'http://powerbi/reports/powerbi/BI/Strategy_Investment/Strategy_Research/For_Strategy_Freeze_detal_upd'
         ),
        ('D105874E-23A4-4651-828B-F9DC6F72279E',
         'http://powerbi/reports/powerbi/BI/Other/Refinitiv'),
        ('E606EC14-1610-4F4F-A3B5-1336C824D6BE',
         'http://powerbi/reports/powerbi/BI/Other/HYS_BP'),
        ('09CE101B-18E5-4575-A344-B46963F6ECD9',
         'http://powerbi/reports/powerbi/BI/Other/HYS_BP_V2'),
        ('7A201C8A-79D5-4EB5-87D7-5C1DBF9389F4',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/HYS_Register'),
        ('962FE522-7A7C-4301-A0B3-6AEB0B400D0F',
         'http://powerbi/reports/powerbi/BI/Finance/Accounting/HYS_Register'),
        ('C78C2BBA-8BD0-4A76-849E-F5B9E3978C6C',
         'http://powerbi/reports/powerbi/BI/Finance/Accounting/HYS_Register_enc'
         ),
        ('068C2661-CDED-4DB5-AB8F-FE5EE3D0DA22',
         'http://powerbi/reports/powerbi/BI/Finance/Accounting/HYS_Register_yeni'
         ),
        ('584C9474-9705-47E7-815F-7D2CAC87C7BB',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/HYS_Kredit_Xetti(esas)'
         ),
        ('86678C38-075F-44DF-B1D8-AB188944B9AD',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/HYS_Kredit_Xetti(esas)'
         ),
        ('BE6DD5D0-11FD-4DCA-B4BD-0B575D7B2077',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Insurance_Risks_Reserving/KHS_data_for_CBAR'
         ),
        ('328B39D3-D1F3-4FB3-98E5-35E25F577A4F',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Yeni_CRM_XitamdanYayındırma'
         ),
        ('5C5EA964-28FF-449D-A782-2DA29E224F16',
         'http://powerbi/reports/powerbi/BI/IT/Reshad_UPR_Sehf'),
        ('FC773B86-71DE-42A0-8042-3DCC10E5F358',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Insurance_Risks_Reserving/Reserve_Check'
         ),
        ('B7604C18-4177-43F3-ABE0-6B830560062C',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Underwriting_Reinsurance/TLS_policy'
         ),
        ('153C100F-15CE-4764-922B-29A65DB18C3B',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Insurance_Risks_Reserving/Ehtiyatların_A.'
         ),
        ('0B8EAF02-C426-4CE2-9052-16CA8DDEB807',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Insurance_Risks_Reserving/Məhsullar Bütün Sütunlar/MLİ_butun_statuslarla'
         ),
        ('4EE44537-1445-4612-9D18-FE5D750AA075',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Insurance_Risks_Reserving/Məhsullar Bütün Sütunlar/HYS_butun_statuslarla'
         ),
        ('F7044E39-AC53-4CB8-8ECA-9EB663DD278B',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Insurance_Risks_Reserving/Ehtiyatlarin_A(HYS)'
         ),
        ('A696724A-3D0C-4854-BAFA-1EF7449E8A9E',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/BP'),
        ('89F46C2B-1BAC-4FC3-A3F6-F20ED22A3309',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/PH_HYS_Bonus'),
        ('3EAF1804-49D4-48F0-B81F-71C864CC0A47',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Support_to_Insurance_Operations/GHS_copies_report'
         ),
        ('7C1830EF-C383-460F-803B-1936C8348BA0',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/NSSP/GHS_prolongasiya'
         ),
        ('BA8BB974-308A-4B7E-B6D0-98DADD42BFC2',
         'http://powerbi/reports/powerbi/BI/Sales_Marketing/Tele_Sales/FHS_Müqavilələr'
         ),
        ('5A09A948-8B05-4C68-8418-EEA96067E558',
         'http://powerbi/reports/powerbi/BI/Agile/HYS/underwriting_tekrar_muraciet'
         ),
        ('9CE843CC-C7E6-40E2-8490-70BB78BDD981',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Underwriting_Reinsurance/Monthly_Bordero'
         ),
        ('2A3E50D9-710F-4819-8352-0DA06DDD555C',
         'http://powerbi/reports/powerbi/BI/Other/Sanan/CRM_Müraciətlər'),
        ('CD2C9443-80DB-488E-896A-AF18D454662D',
         'http://powerbi/reports/powerbi/BI/Other/Sanan/CRM_Hesabat_HYS'),
        ('FAB92B07-F3A8-41E5-8C35-63AA1B24C5CD',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Underwriting_Reinsurance/Ander_emekdaslar_muqavileler'
         ),
        ('0C15BE42-F878-4221-80BC-EEA5DD5903DE',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Claims/HYS_Claims_report'
         ),
        ('2E66EC2B-64FC-4789-8100-D6035972E1F2',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Pricing_Portfolio_Analysis/HYS_Risk_mebleg'
         ),
        ('2A6A1AC5-7B35-4AAF-8858-CF35B4471002',
         'http://powerbi/reports/powerbi/BI/Other/Legal_Support/KHS new customer'
         ),
        ('191DF0E8-3CC7-4730-9888-12E9368BC06E',
         'http://powerbi/reports/powerbi/BI/Sales_Marketing/Marketinq_mahsulun_inkishafi/Teklif_sorgu'
         ),
        ('C98A2811-6DDC-4301-823C-1218D1C1B0D1',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/HYS (CPA olmayanlar)'
         ),
        ('01474B85-9530-413F-9A81-B4B79FE30CBA',
         'http://powerbi/reports/powerbi/BI/Strategy_Investment/Strategy_Research/Claims_Data'
         ),
        ('6D430DC0-A552-406B-B9E6-6BF56E1A9401',
         'http://powerbi/reports/powerbi/BI/Other/Sanan/CRM_Zənglər'),
        ('D1484088-0BCE-4D19-ABEA-1B5D2F338CC3',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Claims/Arxiv/Claim_hys'
         ),
        ('3E90134D-654F-4201-AC64-33C8FF5B6371',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Claims/Arxiv/Claim_mli'
         ),
        ('6657C0B9-711B-4B2C-82CD-182913CBE5C8',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Claims/Arxiv/Claim_register'
         ),
        ('D00FF7C9-94DC-4537-835B-E273BEFFB432',
         'http://powerbi/reports/powerbi/BI/Other/CPA SQUAD REPORTS/Cpa_Yenilenme_Strateji_agent_shirketler_istisna'
         ),
        ('83C8F52B-778B-4533-92E2-D736760ED6A8',
         'http://powerbi/reports/powerbi/BI/Other/CPA SQUAD REPORTS/CPA_Yenilnmə'
         ),
        ('03F4F2ED-1A57-4C4B-804C-5FA34D49F4B9',
         'http://powerbi/reports/powerbi/BI/Other/CPA SQUAD REPORTS/Cpa_all_insurance_policy'
         ),
        ('65BCACB2-B7DE-467A-B32B-270FA6EEB532',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/HYS_tel_mob_email'
         ),
        ('2D99C5F4-6EF7-4E07-B74B-F981FA4A0B0F',
         'http://powerbi/reports/powerbi/BI/Product_Improvement/MLI_aktiv_claim_xitam'
         ),
        ('8879B099-BC1B-407D-A57B-605BB169E68B',
         'http://powerbi/reports/powerbi/BI/Agile/HYS/BP bonus'),
        ('CD321899-CF36-4E49-A325-0040F82FCDAD',
         'http://powerbi/reports/powerbi/BI/Agile/HYS/Dekabr bonus'),
        ('34F879A0-7D0F-4389-AE20-8A6348E9B709',
         'http://powerbi/reports/powerbi/BI/Other/HYS_Customers'),
        ('3B34A65A-011D-4DA8-A820-FD05217FB77A',
         'http://powerbi/reports/powerbi/BI/Other/CPA SQUAD REPORTS/Agent_report_for_MXS_'
         ),
        ('FE6D363A-526C-491A-AC58-B9E9B558B027',
         'http://powerbi/reports/powerbi/BI/Agile/HYS/Online_kalkulator'),
        ('6FBBA9EF-8AC0-459C-A67F-AEE1C7D7BA45',
         'http://powerbi/reports/powerbi/BI/Finance/Financial_Supervision/LMS_Company_Contract'
         ),
        ('332F6A1F-6F5B-42EB-9526-2073FFDA3852',
         'http://powerbi/reports/powerbi/BI/Sales_Marketing/Tele_Sales/Telesales_lead_report'
         ),
        ('2B3FE642-BB1E-4332-8555-CD8FEFF7BAA9',
         'http://powerbi/reports/powerbi/BI/Agile/HYS/Tracking'),
        ('4981175A-1D82-491D-8D48-B51443698237',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/Yeni HYS müştərilərin zəng müraciət sayı - 2023'
         ),
        ('7660637E-E552-4D47-906F-50013B083D9F',
         'http://powerbi/reports/powerbi/BI/Other/Sanan/CRM_Müştərilər'),
        ('0D5DC0FE-D945-488A-87FC-47D718BC2745',
         'http://powerbi/reports/powerbi/BI/Agile/HYS/Hys_upsale'),
        ('B221DB38-BC93-4F47-97A0-C40270630827',
         'http://powerbi/reports/powerbi/BI/Agile/HYS/Online_tamamlamayanlar_all'
         ),
        ('6FD348C6-B56E-4886-8E2C-19B14C523C9C',
         'http://powerbi/reports/powerbi/BI/Agile/HYS/Online_tamamlamayanlar_Sales_Squad'
         ),
        ('57CC0787-2650-4FB7-846D-9A8CE37A131B',
         'http://powerbi/reports/powerbi/BI/Agile/HYS/Online_tamamlamayanlar_Telesales'
         ),
        ('2329C347-2792-46C3-885F-A5031345202C',
         'http://powerbi/reports/powerbi/BI/Agile/HYS/MX_online_muraciet'),
        ('BE74D2BC-2DB0-4C6B-AF83-161653061969',
         'http://powerbi/reports/powerbi/BI/Sales_Marketing/Banks/MLI_Debitor_tools'
         ),
        ('129D15EA-8D35-4C59-800A-F302AB371CB9',
         'http://powerbi/reports/powerbi/BI/HR/Turniket Overtime'),
        ('26BE9EB8-8D8B-42E2-A0C3-12D69B51ABD7',
         'http://powerbi/reports/powerbi/BI/HR/Turniket_Gecikme_TezCixmaCemi'),
        ('D06A8077-9072-49D6-9D14-89CCA20F0047',
         'http://powerbi/reports/powerbi/BI/test/Turniket_Gecikme_TezCixmaCemi'
         ),
        ('B116271F-EC2E-41F5-84A3-0CF980873731',
         'http://powerbi/reports/powerbi/BI/HR/iscilerin_is_saatlari'),
        ('DEA62B90-54CE-4DE3-90EA-3AC98B64ECB5',
         'http://powerbi/reports/powerbi/BI/HR/Turniket_total'),
        ('BA07F2E1-55CB-4062-9D71-D00B38B0D087',
         'http://powerbi/reports/powerbi/BI/IT/PermitData'),
        ('F62C3422-8F42-49D6-BDB4-B1ADE309EE74',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/CRS Fatca'
         ),
        ('0B8BFE0A-7323-4419-AE06-CDBD76536CAF',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/CRS Fatca (3)'
         ),
        ('C28B405B-08C0-4969-AAEE-0BC405A2CB64',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/PI_Sorghu'
         ),
        ('5884066E-86E9-4EFA-900C-9AFDD737BA33',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/PI_Sorghu_mno_sh'
         ),
        ('8B8E6966-8E3B-41BD-B1AA-6EA8BFC8E478',
         'http://powerbi/reports/powerbi/BI/IT/PI Sorğu'),
        ('6508A77B-7DF1-4154-B090-8D876ECEF4B5',
         'http://powerbi/reports/powerbi/BI/Other/HYS_Recommendation'),
        ('68B88D6A-EB51-4DD9-B743-66DD1C421130',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Claims/Arxiv/HYS_Claims_report_upd'
         ),
        ('056BA66C-2AB5-4267-9647-963A7D50E117',
         'http://powerbi/reports/powerbi/BI/Finance/Financial_Supervision/Debitor/MLI_FHS_APG_debitor_rac_limetlere_nezaret'
         ),
        ('2B2EB80C-3729-4396-AAA7-4982F147B942',
         'http://powerbi/reports/powerbi/BI/Finance/Financial_Supervision/Debitor/Debitor RAS/MLI_FHS_APG_GHS_debitor_borc'
         ),
        ('D579DC92-9189-4DC0-A3D9-5AC49094542C',
         'http://powerbi/reports/powerbi/BI/test/Elsun_debitor/MLI_FHS_APG_GHS_debitor_borc (1) (1)'
         ),
        ('E315C199-5FFD-4063-9853-82C3FF88FD84',
         'http://powerbi/reports/powerbi/BI/Other/Sanan/HYS_xitam_rüb'),
        ('9F0D49A0-E4A4-4D20-A46C-869F805AD8D3',
         'http://powerbi/reports/powerbi/BI/Other/Sanan/HYS_sığortalı_dəyişikliyi'
         ),
        ('05E9E8DF-EE0D-4A95-B13D-A9948F9D3A61',
         'http://powerbi/reports/powerbi/BI/test/Fatima/Salary'),
        ('4BE0D8F0-2326-40D0-AF28-ADC75A9D460B',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/HYS_Renewall_All_Data'
         ),
        ('6FFE0982-D47D-4A63-95FC-97B0992A9833',
         'http://powerbi/reports/powerbi/BI/Agile/HYS/Website consultation'),
        ('C17AB8DB-70D4-4983-966E-B76EDEFDE29E',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Underwriting_Reinsurance/Icbari_Fakultativ'
         ),
        ('1732B5C0-9588-49FD-AEAE-8FC98F1720E4',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Underwriting_Reinsurance/Icbari_Fakultativ_Ayliq'
         ),
        ('F04F3613-923A-4CBA-93DD-46323184FBA6',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Underwriting_Reinsurance/Icbari_Register_for_Re'
         ),
        ('28750F45-2A2E-480D-A651-8DE8D9343A49',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/HYS_aperator_Mxs(5)'
         ),
        ('63563672-F359-4D5E-9C80-482DCE3CAE1A',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/GHS Debitor'),
        ('47DED857-0F65-494D-A0A8-EE551C837AF2',
         'http://powerbi/reports/powerbi/BI/Other/Sanan/Сompany_addresses'),
        ('9861D9EA-8EE2-4DC6-BF6C-E01742A23B28',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Insurance_Risks_Reserving/Korparativ_Register_V2'
         ),
        ('FF0F0AC7-CD15-436B-876E-A261442200D2',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/K2/K2_CPA'),
        ('463ACFB3-850D-4CA4-9ED2-CBE74991B835',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/K2/K2_KHS'),
        ('109960C7-54BE-43A0-B8E3-F27F72175DE9',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/K2/K2_MLI'),
        ('BFD30FC7-74CD-4C62-BF67-207CC80AEF04',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/Kurator_Musteri'
         ),
        ('ECEA23B1-031B-48B1-AC1F-6DE865368BAC',
         'http://powerbi/reports/powerbi/BI/Other/CPA SQUAD REPORTS/CPA_Yenilnmə_2021_11_30 version'
         ),
        ('C5731CFD-D1FA-4348-8A14-73080AEBF478',
         'http://powerbi/reports/powerbi/BI/Strategy_Investment/Strategy_Research/CPA_renew'
         ),
        ('7E5D28AA-2E1F-4972-827A-7BB61FA9D727',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/HYS SM və SH'
         ),
        ('F0085401-77D0-43E4-9E7C-BCE04BF57469',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/Application'
         ),
        ('2FC21029-7A49-45C4-932E-D20279A6E6D9',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/k2dac_balance_gwp_base_all'
         ),
        ('320AAFF2-3D00-42D4-9D95-ACA26599C0B0',
         'http://powerbi/reports/powerbi/BI/Finance/Financial_Supervision/k2dac_balance_gwp_base_all_for_Audit'
         ),
        ('AA31C1E3-E3C4-418A-A41B-DD7C20E5A69F',
         'http://powerbi/reports/powerbi/BI/IT/Agile'),
        ('AED3C699-978E-4867-8C04-CAD40ACF0387',
         'http://powerbi/reports/powerbi/BI/IT/Agile2'),
        ('A9CCAE66-3402-4E77-A203-92C7E0679A3A',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/SalesApplication'
         ),
        ('612BD33B-3AD1-4524-AB37-7373BB75356F',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/SalesApplicationCompany'
         ),
        ('6BC56D49-E3B8-4BBE-BCD4-6F24D5683E78',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/SalesApplicationSeller'
         ),
        ('BD96D07B-7B31-43FB-873B-4B9BD4ADBFCE',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/HYS_Company_Asan'
         ),
        ('E7D94D87-720E-4123-9FDE-01F0E3FE7EEF',
         'http://powerbi/reports/powerbi/BI/Other/CPA SQUAD REPORTS/CPA_tekrarlanan_voen'
         ),
        ('B69E608C-FD35-4BDC-8A2C-F0F4DA00B454',
         'http://powerbi/reports/powerbi/BI/Other/CPA_mno'),
        ('D77E3612-0E29-4045-8CF4-E7587C13FAF2',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/CPA_Renew_Date'),
        ('B114E132-7C46-4A0E-9BAB-DF2D7F579119',
         'http://powerbi/reports/powerbi/BI/Other/CPA SQUAD REPORTS/CPA_sales_monthly'
         ),
        ('D90F2A89-26B6-4F70-AEC1-EE9293943C20',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/CPA_Xitam'),
        ('8E87B48A-1ED2-4D88-8069-53E9946E3584',
         'http://powerbi/reports/powerbi/BI/Other/CPA SQUAD REPORTS/Cpa_Yeni'),
        ('6F96CA6D-69CE-4299-B5C8-AE7ECC09EFB3',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/CPA_Yeni_Yenilənmə'
         ),
        ('D68C4DB2-9EFA-4B8F-A053-2D342F26A261',
         'http://powerbi/reports/powerbi/BI/Finance/Accounting/ESMN_hesabat'),
        ('CEEF07CC-C21D-451E-B20C-9C31707FBDF2',
         'http://powerbi/reports/powerbi/BI/Finance/Accounting/ESMN_hesabat_v2'
         ),
        ('7D9671FF-557D-4F32-9D7E-A87C7D17A576',
         'http://powerbi/reports/powerbi/BI/Finance/Accounting/ESMN_hesabat_v2_1'
         ),
        ('A95FF78C-E6CF-4299-BEE2-5190D73767E6',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/Icbari_Status_Register'
         ),
        ('FBCB6ABA-4984-4F8B-9DA4-3729038B4733',
         'http://powerbi/reports/powerbi/BI/test/Icbari_Status_Register_Cumulative'
         ),
        ('F4B93B68-6674-4453-B73C-390B96B8CEF0',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/Icbari_Status_Register_VUSAL'
         ),
        ('88E14D5D-F8AA-46D6-9655-BD1DDB8E13D5',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/HYS_active_Sirket_tarix'
         ),
        ('48C8CDCF-8335-4436-B830-0BB9D43B160B',
         'http://powerbi/reports/powerbi/BI/Sales_Marketing/Marketinq_mahsulun_inkishafi/Shaxsi_kabinetde_recomendation'
         ),
        ('CD2E183B-F350-4E8D-A2A6-3EA87948AC9C',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Underwriting_Reinsurance/Hys_Apg_FHS_BH_teminatli_muq'
         ),
        ('D04F0D9C-BFE0-4715-AD0F-F94A86D2F045',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Pricing_Portfolio_Analysis/Icbari_for_ISB_with_date'
         ),
        ('8FF551D5-DBC5-4E7A-A30C-0610FC47BBEE',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Pricing_Portfolio_Analysis/Icbari_for_ISB'
         ),
        ('7162E4B4-5972-46F7-BA4C-867A5608DC58',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/Company_Payment(Company Count)'
         ),
        ('AD7D6EC2-1D03-4DA2-A7E9-55824CE7D2AC',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/Company_Payment(esas)'
         ),
        ('9A7069FB-C578-46DF-BA76-6AF092D0C9DC',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/HYS_shirket_ishchi_sayi_aktiv'
         ),
        ('333BF786-DD59-4ED6-ACC3-FE16220EADA9',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/HYS Aktiv Musteri Sayi'
         ),
        ('7AECFEA9-7775-49AA-8E82-A98B89EBAFD7',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Call_Centre/Call_Centre_Claim_Result'
         ),
        ('F47D6B5E-DF97-476F-94BD-13FEF99BB159',
         'http://powerbi/reports/powerbi/BI/Strategy_Investment/Strategy_Research/Aktiv_pin_mehsullar_uzre'
         ),
        ('69F0D004-28B4-4CA2-B930-31A28FA0949E',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/HYS_PIN_i_standart_olmayan_mugavilelerin_siyahisi'
         ),
        ('1632636D-5BE0-4CD5-ADD8-A28CDAAABE56',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/NEW_Balance_for_MCKinsey'
         ),
        ('5C1F1A7E-7342-4A37-B68A-E705F97EF51A',
         'http://powerbi/reports/powerbi/BI/Finance/Financial_Supervision/HYS_Budget_for_Finance'
         ),
        ('7203E70D-4D73-4007-A1C8-19D61EDF1CE9',
         'http://powerbi/reports/powerbi/BI/Other/Legal_Support/Daily_new_customer'
         ),
        ('80710F04-8878-481E-ABCA-37FEDED78D35',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/HYS_Claim'),
        ('BCA57C14-6C22-439A-9E9A-B67D55C113F8',
         'http://powerbi/reports/powerbi/BI/Strategy_Investment/Investment/HYS_GWP_BUDGET'
         ),
        ('83CFD067-DCC7-4FE9-A1D1-75C0B896DA66',
         'http://powerbi/reports/powerbi/bi/hr/Incentive/HYS_ReNEW'),
        ('7B638B10-39AE-4F11-AE05-1A5EF7B6DF67',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/HYS_scan_file(Pincode_esas_2)'
         ),
        ('FA6A607A-60D7-4597-A561-689871567FCF',
         'http://powerbi/reports/powerbi/BI/Strategy_Investment/Strategy_Research/HYS_Xitam'
         ),
        ('AB554EA7-75D3-43E1-A43B-624F5B3C0BAB',
         'http://powerbi/reports/powerbi/BI/Other/Legal_Support/New_customer'),
        ('DA182AD1-5B6F-4DDC-8EAE-155732E66E00',
         'http://powerbi/reports/powerbi/BI/Sales_Marketing/Marketinq_mahsulun_inkishafi/Şəxsi_Kabinetdən_istifadə'
         ),
        ('339B2748-324A-4A16-B076-B4BCEC70AE9D',
         'http://powerbi/reports/powerbi/BI/IT/Musteri_Muraciyet_ASAN'),
        ('4644849A-A4EB-4F9E-8482-E035F3521CBA',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Underwriting_Reinsurance/Aktiv_(secilmis_tarixlerde)_mugavileler_uzre_sm_gwp'
         ),
        ('DEAC581D-EFC2-4C6F-BCDE-EB10AC7FB03C',
         'http://powerbi/reports/powerbi/BI/Strategy_Investment/Strategy_Research/HYS_Icbari_Aktiv'
         ),
        ('42192398-FBB9-45C9-9D59-8E9291A51A97',
         'http://powerbi/reports/powerbi/BI/Strategy_Investment/Strategy_Research/Icbar_HYS_Pin'
         ),
        ('C07F9121-06F7-4E7E-A116-1276846A11CE',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/HYS_GWP_Paid'),
        ('BB77A9F5-84C8-40F7-980E-5C604C4EF7FD',
         'http://powerbi/reports/powerbi/BI/test/Weekly_reporting_data'),
        ('71C3B7DD-6BB5-475E-BB60-BE8426A11438',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/GWP_korparativ_tarix_araligi'
         ),
        ('D2FC6C3F-A0C3-49C6-A8C1-87ED9A0233E9',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/HYS_scan_file(esas)'
         ),
        ('76ADE0D9-5D1A-4D0B-9812-1D92B0C0CECA',
         'http://powerbi/reports/powerbi/BI/test/Weekly_reporting_data_k2'),
        ('8CC589D3-0FBB-4F0B-9D42-FA035247CCD1',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/CPA_(HYS-si_olmayan)'
         ),
        ('D646D816-1C72-4A8B-9257-5C144F27B07E',
         'http://powerbi/reports/powerbi/BI/Agile/HYS/CSI'),
        ('01F24EA8-30F4-4139-A99B-75F0568E939F',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/NSSP/GHS Report Yeni_Yenilenme'
         ),
        ('BB22E0DF-B221-4C9A-BCE1-950335FBC0E0',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/GHS_Yeni_say_Yenileme_say_from_Dashboard'
         ),
        ('6C72CB2A-25C8-4C6C-93FB-2CA9073AE27A',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Insurance_Risks_Reserving/Reserve'
         ),
        ('8B40C7ED-24A3-4B0F-8F74-64DE8D0175AC',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/Rezerves_by_products'
         ),
        ('21389429-DA9C-4837-AB1C-6BCD1AD2627D',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/Ehtiyatlar'),
        ('C769F328-75DC-436F-959B-1ABD3E4B063E',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Insurance_Risks_Reserving/Icbari_UPR_V2'
         ),
        ('5A46C6BC-A769-4143-B2C0-2B02EAC0D4A1',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/Icbari_hys'),
        ('27C80D4A-6882-420D-8251-0B5DE582A6D0',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/CPA_Debitor_Class'
         ),
        ('DC9D3FD9-3163-4196-BC9D-481F76A12AFF',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/Icbari_yenileme'),
        ('23DE67C5-A6DD-467E-8B05-093320A71599',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/HYS_Sales'),
        ('66586499-77AC-4BB7-A117-D1506F40BEA5',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Pricing_Portfolio_Analysis/Icbari_Register'
         ),
        ('ACE91644-DFA6-41AB-BE6E-D9B694010A7D',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Pricing_Portfolio_Analysis/Icbari_Register (3)'
         ),
        ('52964780-916D-424A-815A-11FB18009581',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Pricing_Portfolio_Analysis/Icbari_Register all'
         ),
        ('E2F5F802-89C7-4346-ABC9-B5B39975EB95',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Pricing_Portfolio_Analysis/Icbari_Register_for_audit'
         ),
        ('0F80F642-37CB-484F-A9C5-E5D26947401B',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Pricing_Portfolio_Analysis/Icbari_Register_for_audit_all_companies'
         ),
        ('4BDCE3BC-63B3-4A4B-9F80-F752CD02520E',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/NEW_Balans'),
        ('0B9C6A71-5857-4241-A9FD-3F8E32EDD8A5',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/HYS_claim'),
        ('2824C120-791D-402C-994F-C2A61B2808E4',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Operational_Risks_Management/Icbari_Claim'
         ),
        ('C1408995-14F2-4D0F-AB92-3974A1F12952',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/K2raport'),
        ('53EDC37B-011C-4752-AB22-C7C92697D3B7',
         'http://powerbi/reports/powerbi/BI/Other/K2raport_by_mno'),
        ('D6D4971D-29F3-4AFB-A77D-D8FC52949C68',
         'http://powerbi/reports/powerbi/BI/Other/CPA SQUAD REPORTS/Elave_Buraxmayan_Müqavilələr'
         ),
        ('10752468-7AF8-4067-8B02-569FA5FA7DC2',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/HYS_bank_kredit'
         ),
        ('B75B7FAE-8BD5-4351-BA06-C2722236F615',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Support_to_Insurance_Operations/HYS_Scan_Asan'
         ),
        ('0CB7CBD8-CE55-4CA3-8CCD-B03E8CBE0AA0',
         'http://powerbi/reports/powerbi/BI/Strategy_Investment/Strategy_Research/HYS_Customer_Count_Details'
         ),
        ('01FD7D1A-9E90-452D-8D55-513612110168',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/Kredit_Goturen_Mushteri_Melumatlari'
         ),
        ('C2E822A3-CA53-4984-8F4B-A6F077797BB4',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Pricing_Portfolio_Analysis/KHS_Register'
         ),
        ('4EFB5F69-A25D-4B34-B248-8ED4FF2470B5',
         'http://powerbi/reports/powerbi/BI/Other/KHS_Register_For_Audit'),
        ('D775130D-6092-4119-9BD8-85AC3E6B648D',
         'http://powerbi/reports/powerbi/BI/test/vintaj_data_khs'),
        ('3629B4E0-8707-450E-9C23-F891368AFAA7',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Pricing_Portfolio_Analysis/vintaj_data_khs'
         ),
        ('3E44CE11-2ABF-4A37-A09B-61D88FFBB442',
         'http://powerbi/reports/powerbi/BI/test/Icbari_Status_Register_with_other_sheets'
         ),
        ('D2821E79-6B00-4D61-B731-E7B344EDBCB3',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/Icbari_Status_Register_Cumulative'
         ),
        ('E6AFFC14-8AD4-4750-AB15-7B83F3A6A456',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/Icbari_Status_Register_with_other_sheets'
         ),
        ('E113945D-F669-42A8-B8F0-1D49C5950D84',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Pricing_Portfolio_Analysis/MLi_comprehensive_solution'
         ),
        ('0B7F5A53-6BB4-4C20-96E8-1047BB509CDA',
         'http://powerbi/reports/powerbi/BI/Finance/Accounting/HYS_Kuratorlar'
         ),
        ('4F7F1E84-C36B-4A79-A446-D77D4F9C6D47',
         'http://powerbi/reports/powerbi/BI/Agile/HYS/Claim not renewed'),
        ('47716EAD-4C7B-4B8F-A6D7-D197E97F5874',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Support_to_Insurance_Operations/Copies_Raport'
         ),
        ('CD94317C-476F-4ABA-B208-324242BAAEEB',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Support_to_Insurance_Operations/Copies_Raport_onceki_tarix'
         ),
        ('6E8FA87C-4122-4025-936D-4A44C8A8FC59',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/HYS_scan_File_CRS_Raport_detailed'
         ),
        ('6EF4058E-CE68-4D47-AD72-37B0EAB74439',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Operational_Risks_Management/NPS'
         ),
        ('BE2BC0D1-EFCE-4ADB-A0EB-D31A0F9CFAA4',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/Arxiv/HYS_Register_Arxiv'
         ),
        ('C856B38B-2190-4F95-A241-E364D1194CAB',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/HYS_shirket'
         ),
        ('39ABBCF5-4657-409F-B8CA-D59F74DDF239',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/Sap_Customer'),
        ('C181D052-028B-4206-85B9-7469FE349A00',
         'http://powerbi/reports/powerbi/BI/Sales_Marketing/Marketinq_mahsulun_inkishafi/MyLife_muraciyetler'
         ),
        ('D09CA9B7-E617-463E-9504-BDDEFBB75537',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/2022_4Q_Kam1_Kam2_Kam3_TeleSales_birdefelik'
         ),
        ('2C184216-B611-4374-AF8E-0133610F9B95',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/2022_4Q_Kam1_Kam2_Kam3_TeleSales_hissevi'
         ),
        ('3C3D6618-767D-426B-8DC3-F708FE18CBA7',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/2022_4Q_Mx_0_30_0_45'
         ),
        ('8807DBB5-9C65-4C46-B41F-06F4C8186BB6',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/2023_1Q_Kam1_Kam2_birdefelik'
         ),
        ('65A4506E-433B-438F-913D-7BD727439EEB',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/2023_1Q_Kam1_Kam2_Kam3_TeleSales_hissevi'
         ),
        ('E02B5713-B690-46AC-8A6A-C99E53278C70',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/2023_1Q_Mx_0_30_0_45'
         ),
        ('CD6C47A1-65EF-473F-AD42-519D9213EAA3',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/2023_2Q_Kam1_Kam2_Kam3_TeleSales_hissevi'
         ),
        ('06CAC6BD-3082-435F-BC24-A752256049C7',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/2023_2Q_Kam1_Kam2_TeleSales_birdefelik'
         ),
        ('360E878A-3D1A-4B10-8018-DC67C2E211A6',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/2023_2Q_Mx_5_30'),
        ('F2D6D36A-14FB-4A2A-B261-8F28521DFDA1',
         'http://powerbi/reports/powerbi/BI/Strategy_Investment/Strategy_Research/Aktiv_cpa_fn_maas_sh'
         ),
        ('434681C2-F3CD-4427-8A94-C41F30D73FDE',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/ApplicationType'
         ),
        ('7804E499-66AA-4257-98EE-0C61DB62AB28',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/test/Copy of CPA_Debitor_KPI_10_21'
         ),
        ('9D1C1E0B-D32F-4085-881F-C64D04AC9E3F',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/CPA'),
        ('F1B951C0-2D31-4A54-AC31-EE82B7D558E8',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/CPA_Debitor_KPI'),
        ('B2C291C0-C413-4DFA-BC14-39A9692E757D',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/CPA_Debitor_KPI_2022_Q1_Result'
         ),
        ('84C43883-8D5A-434E-947A-AB83F339DAF3',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/CPA_Debitor_KPI_raw_data'
         ),
        ('7799E4BB-99D8-425A-BEB9-09C99CBD8403',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/CPA_Debitor_KPI_raw_data_2Q_birdefelik'
         ),
        ('2FFD1D28-A9EF-48D5-9236-3F5B8E5C68C6',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/CPA_Debitor_KPI_raw_data_2Q_KAM1_KAM2_hissevi'
         ),
        ('926F1B60-5397-40DC-A62F-41EF2E4C3006',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/CPA_Debitor_KPI_raw_data_tarix_mugavile'
         ),
        ('1193BFD8-CE5C-4E78-840A-0D2B5CA5362A',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/CPA_elave_uzre_GWP'
         ),
        ('03162266-C4E7-4CCD-B2CE-60B0B2D87A5D',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/CPA_Fealiyyet'),
        ('482D465F-1923-4E1E-A10B-5A35D92D797F',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/cpa_kurator'
         ),
        ('96A13656-AAF8-4142-A3B2-F711912466D2',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/CPA_sh_paid_debitor'
         ),
        ('AB0DA947-1CB7-45B3-927A-E4BEA21A10B4',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/Customer_category'
         ),
        ('5E65356E-84C5-4AFB-8DC1-120F24EEB19D',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/Daily_sales_and_claim_data_for_holding'
         ),
        ('E2B63746-3603-4FA8-969A-7190DA565448',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/For_Zakir_CPA'),
        ('7A3E7D9C-959A-424B-A55E-35E2BFCD4CCE',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/For_Zakir_CPA_ALL'
         ),
        ('C178A5DF-C845-4229-82A7-342C97916576',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/NSSP/GHS_KB_leaderboard'
         ),
        ('9D48F6BD-524F-4DC2-A85C-7E0634CAA564',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/NSSP/GHS_Motivasiya_Hesabat'
         ),
        ('184FD0C6-80B1-44AC-AD7B-DE1BD65E7B73',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/Gilan_group_mno'
         ),
        ('901DDA8C-AB67-41E4-AE68-6334FC069619',
         'http://powerbi/reports/powerbi/BI/Other/Legal_Support/Huquqi_shexslerin_daxil_olma_tarixi'
         ),
        ('7C11AEAB-16A7-47E9-A695-BC52ECEDA603',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Operational_Risks_Management/hy_qosma_2_new'
         ),
        ('FB07C411-155D-4370-8E85-7B94B77CFD99',
         'http://powerbi/reports/powerbi/BI/Finance/Accounting/HYS tranzit yoxlanış'
         ),
        ('9AEDB8E3-AA08-4A39-B8FC-62DF8D2D2F04',
         'http://powerbi/reports/powerbi/BI/Finance/Accounting/HYS_Bonus'),
        ('C0389A4B-2DCA-40BC-A9C6-27F2F3C50964',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/HYS_bonus_company'
         ),
        ('FBFD6FF0-0DB2-4DA9-95F2-2933AC147111',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/HYS_bonus_company_Backup'
         ),
        ('9D8A9D92-5A8E-425C-9090-28BE84975034',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Pricing_Portfolio_Analysis/HYS_Bonus_Rie'
         ),
        ('9AD0B064-D1E2-45FC-840A-4FECF8D47917',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/HYS_Company'),
        ('DAD26073-FA9C-45A0-B36B-F0655983956D',
         'http://powerbi/reports/powerbi/BI/Sales_Marketing/Marketinq_mahsulun_inkishafi/HYS_Convert'
         ),
        ('22E2CE59-7084-4B23-9F0F-8F5E3AC20D7E',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/Hys_GWP_Cpa_Gwp'),
        ('2DD87520-3EAE-40FC-810C-700AC2FF5476',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/HYS_GWP_date_range'
         ),
        ('B8E638DD-B44A-4A44-8216-926DB9C3519E',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Claims/Hys_hesab_nomreleri'
         ),
        ('14D2449C-5965-4D8E-9AF4-9A4167E959E5',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/HYS_Icbari_company'
         ),
        ('F77D642D-C6E7-47B4-854D-00B892CB107B',
         'http://powerbi/reports/powerbi/BI/Strategy_Investment/Strategy_Research/HYS_Icbari_company_for_exact_date'
         ),
        ('1069FE63-254D-4DED-BBAA-3C44E02D3B4C',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/HYS_Kurator'),
        ('9F3B2B37-1775-405F-914C-C0E2D541F2CE',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/HYS_kurator_maas_info'
         ),
        ('A0D73B20-F085-4BF6-A30B-A80D326A4A91',
         'http://powerbi/reports/powerbi/BI/Other/Legal_Support/HYS_musterilerin_shirketler_ve_qosulma_tarixleri'
         ),
        ('410032B0-8570-4F43-9029-F9D491E1AFD5',
         'http://powerbi/reports/powerbi/bi/hr/Incentive/HYS_New_Company'),
        ('943F376A-61D4-4A83-9E5F-B663A1CD596E',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/Hys_Paid_Cpa_Gwp'
         ),
        ('B540CF15-00C4-4D5E-83C4-8C27BA23DD1F',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/HYS_Prolongation'
         ),
        ('EFBEF3B2-B8AB-4C96-B9C0-DF0FE1C3E4F6',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/HYS_Retention_Contract'
         ),
        ('DA9F4673-1AF6-4A30-B481-A531E7B735A3',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/HYS_SH'
         ),
        ('C5D56336-46F9-48A7-9216-B34C08863876',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/HYS_Type'
         ),
        ('3BF7EBB5-A804-4CA3-8BF1-34CFFC4AD7C2',
         'http://powerbi/reports/powerbi/BI/Finance/Accounting/HYS_Xitam'),
        ('0C54FD32-E642-4B66-83D7-01104809F87E',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/HYS-ye_qoshulma'),
        ('4F8D221C-58BF-41E2-B9D2-C93B026F0708',
         'http://powerbi/reports/powerbi/BI/Finance/Accounting/K2 raport for Audit'
         ),
        ('F0D9C5B5-05AD-4532-9EEB-B4912B2F597F',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/k2dac_balance_all'
         ),
        ('149F3B88-BFCA-4DF5-89BB-78598AA58C96',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/Kredit'
         ),
        ('0A3DFB43-5CE3-4531-8758-645FCC57E93A',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/Kredit_Upd'
         ),
        ('28C36D1F-BC8A-41DD-9A30-8E41C2FFD6A2',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/Kurator for Company'
         ),
        ('15D9A32F-54BE-45B5-B09B-92D1BDFBF1C1',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/Oil_Gas_Companies'
         ),
        ('71E8A00D-FC5D-4542-B561-16E946FE10E6',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Underwriting_Reinsurance/Predict'
         ),
        ('C6354BA0-5E52-431F-B046-7CC28E9D61D4',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/Predict'
         ),
        ('78ED7C9F-037F-497A-8A62-BED7389E66D5',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/ReNEW_Icbari'),
        ('56748832-5472-4969-8C57-73918E2BA5E3',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/TeleSale_Teminat'
         ),
        ('6F27CD90-7116-47D7-9022-A3C8AC475FDE',
         'http://powerbi/reports/powerbi/BI/Other/CPA SQUAD REPORTS/tesdiqlenmemis_elaveler'
         ),
        ('C3952E6D-F3D4-4A2B-AF27-522010E0B774',
         'http://powerbi/reports/powerbi/BI/Strategy_Investment/Strategy_Research/voen_uzre_mno_detailed'
         ),
        ('7746B372-9373-477E-8808-233BC1FE7879',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/CPA_Debitor_Qarşılaşdırma'
         ),
        ('0FD7C39F-FD53-4A23-9A57-0832183A34DD',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Call_Centre/Daxili_Hesabat'
         ),
        ('09D0A3C8-4AA7-421E-A4AC-73FB07096596',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Call_Centre/Daxili_Hesabat_new'
         ),
        ('89A7EF73-8DF8-489E-A2E5-6260ACAEF273',
         'http://powerbi/reports/powerbi/bi/hr/Incentive/CPA_Müqavilə'),
        ('587CAE6A-44DE-4704-9483-5C42D59090AA',
         'http://powerbi/reports/powerbi/BI/IT/CPA_Yenileme'),
        ('6D47DEA4-E805-48A5-B447-F4371EB0099F',
         'http://powerbi/reports/powerbi/BI/Strategy_Investment/Investment/Konvertarsiya_muracietleri'
         ),
        ('01A541D8-F1E3-417A-9632-14A632E61661',
         'http://powerbi/reports/powerbi/BI/Strategy_Investment/Strategy_Research/VB_CPA_Row_DATA'
         ),
        ('BC7BDF30-2631-42F6-A864-6EAA2528F5C8',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Claims/CPA_claim'
         ),
        ('18A3B9E8-ED47-4C76-B861-6969D28000FF',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Pricing_Portfolio_Analysis/mli_mortality_realization'
         ),
        ('134F33E8-36EA-4BBE-9C30-42526DDA1EC0',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Operational_Risks_Management/HYS_qarant_mektublar'
         ),
        ('6AD51DBE-3346-45D2-BA7B-7381BD9603C6',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Insurance_Risks_Reserving/MLI_Odenishler'
         ),
        ('66CD2CAA-37AA-4A58-9985-3B8BDE3DDBA2',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/CPA_(HYS-si_olanlar)_Grouped'
         ),
        ('CA1BA167-3EBA-4897-ABA5-1BFBC3AEE5BB',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/CPA_(HYS-si_olmayan)_Grouped'
         ),
        ('8404266E-D6C7-4E2E-A3CB-35A5A40525C0',
         'http://powerbi/reports/powerbi/BI/Sales_Marketing/Banks/Bank_melumatlari'
         ),
        ('571F5C13-4F27-43AE-AA5A-352A45860E8A',
         'http://powerbi/reports/powerbi/BI/Finance/Accounting/BOX_Register'),
        ('F98975F1-F36E-4532-AADF-90567A5D4942',
         'http://powerbi/reports/powerbi/BI/Finance/Accounting/BOX_Register_for_encr_project'
         ),
        ('74EF1C64-BB17-47EF-ADDE-BACE33B0F4FD',
         'http://powerbi/reports/powerbi/BI/Other/Sanan/Mli_active_müştəri_email_rüb'
         ),
        ('0B872427-692D-4D54-A551-BBA55CB44673',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/HYS_ReNew_Result_Arxiv'
         ),
        ('BAFAE07A-93C2-40BA-8C22-B748B15B6545',
         'http://powerbi/reports/powerbi/bi/hr/Incentive/HYS_ReNew_Result_HYS_Ferdi'
         ),
        ('7924524C-9543-4310-B9C0-01B0116A183C',
         'http://powerbi/reports/powerbi/bi/hr/Incentive/HYS_ReNew_Result_HYS_SQUAD_1'
         ),
        ('00E71719-F762-4DD2-9355-D298C0477A39',
         'http://powerbi/reports/powerbi/bi/hr/Incentive/HYS_ReNew_Result_HYS_SQUAD_3'
         ),
        ('02E1487D-0471-402F-87F4-BFC477F5D883',
         'http://powerbi/reports/powerbi/bi/hr/Incentive/HYS_ReNew_Result_HYS_SQUAD_alpha'
         ),
        ('685A9D62-978B-404A-AF9B-C80DA53E1585',
         'http://powerbi/reports/powerbi/BI/Other/Sanan/CRS_Report_Detailed_HYS'
         ),
        ('EFE867E8-3775-46E6-882E-8BBE6E5AB253',
         'http://powerbi/reports/powerbi/BI/Risk_Management/HYS_konvertasiya_sh_gwp'
         ),
        ('4E725AE9-4573-4EA2-AA56-D2401B27F936',
         'http://powerbi/reports/powerbi/BI/HYS_debitor_borc'),
        ('65A57591-AFFE-4F1A-984D-538CF5A8C152',
         'http://powerbi/reports/powerbi/BI/test/MLI_debitor_borc'),
        ('8758A597-C548-4177-A462-B4A12DD594F9',
         'http://powerbi/reports/powerbi/BI/Risk_Management/Credit_market_and_liquidity/Detailed_Data_for_restrcted_cash'
         ),
        ('87D3BE9B-2A76-434A-9D3B-F92BAD7657B8',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Claims/Arxiv/Sexsi_kabinet_claim'
         ),
        ('A5C8D6EE-4147-40B7-B58D-088EE0711533',
         'http://powerbi/reports/powerbi/BI/HR/Vacation'),
        ('F7F7166F-5E0A-4A4F-89FD-7C24ABFAB6ED',
         'http://powerbi/reports/powerbi/BI/test/HYS_debitor_borc'),
        ('34F2FFF3-332F-40C6-A58A-B2C4EF6795E6',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Underwriting_Reinsurance/Mugavile_Yukleme'
         ),
        ('B7B333BB-05D7-4EE2-8D47-CA8AD9EB5F1B',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Underwriting_Reinsurance/Ander_emekdaslar_muqavileler(Sorğular)'
         ),
        ('79B91E7A-6F15-4521-BE88-5A25B32E792B',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/CPA_Agent'),
        ('FC5DD0CD-6542-4308-B5A2-244FADA4480E',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Pricing_Portfolio_Analysis/MLI_Report_Muqavile'
         ),
        ('6170DAD2-87E2-4FC1-9CEA-B62C4DF1C463',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Underwriting_Reinsurance/Main'
         ),
        ('44929A8D-48FC-4E41-B877-D337E78325E8',
         'http://powerbi/reports/powerbi/BI/Finance/Accounting/HYS_debitor'),
        ('A2811C55-41D4-4ADF-BBA9-0534E89628BE',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Underwriting_Reinsurance/HYS_Register_for_Anderrayting'
         ),
        ('59FAA49C-A4C6-4725-B9F4-43EAF356331B',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/Azalma_dondurma_sebebleri'
         ),
        ('1B00EAE5-A6FE-4BF1-B9ED-3ED62C698D4D',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Underwriting_Reinsurance/Aktiv_KHS_Müqavilələr'
         ),
        ('229F09F6-556D-4BE0-84C4-EF146559B755',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/debitor icbari'),
        ('F5B7C042-2B5C-413B-9D0E-DA25FD912062',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Underwriting_Reinsurance/KHS_Bordero'
         ),
        ('7515CC53-8EEF-46A8-87F5-38F66C5ED0EB',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Underwriting_Reinsurance/KHS_Bordero_Statik'
         ),
        ('2812BB17-941D-4B82-87A6-48D7ECF17404',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Underwriting_Reinsurance/KHS_Bordero_with_original_tarif'
         ),
        ('26A4FBF1-6257-49CA-926C-CEF8472E5BAA',
         'http://powerbi/reports/powerbi/BI/Other/KHS_Bordero_for_Audit'),
        ('06D5EB57-0690-4368-8CF6-F32386CF1F7F',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Underwriting_Reinsurance/Customer_operations_history'
         ),
        ('4A67F99A-0527-40F6-856D-3447A287D391',
         'http://powerbi/reports/powerbi/BI/test/Customer_operations_history_dwh'
         ),
        ('38E754A2-A598-4411-AF1E-FAE6E806F706',
         'http://powerbi/reports/powerbi/BI/Finance/Financial_Supervision/MLI_Odenisler_V2'
         ),
        ('5C8BB0C8-A387-4CE9-9680-5B70B40D9B09',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Pricing_Portfolio_Analysis/HYS_data_SH_all_addendum'
         ),
        ('4793D73C-CD70-49D9-8B73-EA60B106A08B',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Pricing_Portfolio_Analysis/HYS_data_SH_all_addendum_test_with_duration'
         ),
        ('EE724025-F8E0-4DA1-80CC-DF05B9C31E8A',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/HYS_Passiv_claim'
         ),
        ('191B01DD-FE68-4C29-B3F7-F032424D246B',
         'http://powerbi/reports/powerbi/BI/Finance/Accounting/Cash_Back_Register'
         ),
        ('D8044528-F248-46E4-8F26-D1F06758AD71',
         'http://powerbi/reports/powerbi/BI/Finance/Accounting/FHS_Register'),
        ('66E608CC-7D5E-4B88-926D-5B7DCAFFE902',
         'http://powerbi/reports/powerbi/BI/Sales_Marketing/Banks/Kapital_Bank_mli_mugavileleri'
         ),
        ('B7FA353F-B097-40F8-BB84-AE7A3E47953E',
         'http://powerbi/reports/powerbi/BI/HR/Turniket məlumatları'),
        ('0924904A-B356-4D8B-AE18-78DEB66D65FC',
         'http://powerbi/reports/powerbi/BI/Finance/Accounting/APG_DT_Register'
         ),
        ('B0A6F686-8B0A-4351-9137-5AED9227B69C',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/Icbari Aktiv Isci Maaşları'
         ),
        ('8980A624-2A9E-4803-8B54-0BFA6C670EC1',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/HYS Register'),
        ('57C075BB-0E3B-4AD6-9456-6BEB5271AE09',
         'http://powerbi/reports/powerbi/BI/Finance/Accounting/MLI'),
        ('049BF5E6-E11C-4EDF-B3A6-F66D4C19E320',
         'http://powerbi/reports/powerbi/BI/Sales/Corporate/Icbari_Register'),
        ('623D4F39-092E-4CB2-9DE3-98C423D05793',
         'http://powerbi/reports/powerbi/BI/Finance/Accounting/MLI_Daxili Kredit_Kapital_Bank'
         ),
        ('A6544F1C-4CDA-40E6-AB19-216A877F04B7',
         'http://powerbi/reports/powerbi/BI/test/MLI_Daxili Kredit_Kapital_Bank_v2'
         ),
        ('A5C3616C-4429-45F5-A02D-5195A69E6160',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/PI_Kasko_Emlak'
         ),
        ('35CC2DB5-A774-459E-8DDC-1578C6BB6C90',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/MLI_Register_for_Reporting'
         ),
        ('B552FC3D-B792-4E55-A03D-D8F3F9A1F3F8',
         'http://powerbi/reports/powerbi/BI/Underwriting_Pricing/Underwriting_Reinsurance/HYS_over_61yearsold'
         ),
        ('1963D410-FA2F-45AA-8BF6-86C8AE5D9037',
         'http://powerbi/reports/powerbi/BI/Agile/HYS/Elave_razilashma'),
        ('CE4B6C50-8043-4432-9415-FFC5D7036561',
         'http://powerbi/reports/powerbi/BI/Finance/Accounting/Anderraytin_last_status'
         ),
        ('E7A518F1-332F-4054-AACF-5C6E724E22B0',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/HYS_kredit_xetti_nomreleri'
         ),
        ('FDFB58A3-2689-4916-925F-4FB8082FF08F',
         'http://powerbi/reports/powerbi/BI/Finance/Reporting/Cash_Flow'),
        ('744F1BC6-A324-49B8-90DC-53DB06D27A9B',
         'http://powerbi/reports/powerbi/BI/Customer_Service_Claims_Management/Customer_Service/Gilan_Aktiv_Muqavileler'
         ),
        ('3C7898DD-7EDC-4D8B-8C0D-CBC0CC36B926',
         'http://powerbi/reports/powerbi/BI/Sales/Individual/LMS_Customer_view'
         ),
        ('CEFC2AF6-9CE3-4596-AB7F-C3CB0E6DAA5E',
         'http://powerbi/reports/powerbi/BI/Other/LMS_All_Status'),
        ('249B77E1-D204-4D7C-A570-20A942CA43EC',
         'http://powerbi/reports/powerbi/BI/Finance/Financial_Supervision/LMS_Customer_Contract'
         )
    ]

    # Current date and time
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Generate tasks data
    tasks_data = [{
        'title': title,
        'description': description,
        'created_at': now,
        'status': False,
        'completed_at': None,
        'completed_by_id': None
    } for title, description in titles_and_descriptions]

    delete_all_tasks(conn)

    # Insert tasks from the predefined list
    insert_tasks_from_list(conn, tasks_data)

    # Optionally display all tasks to verify
    display_tasks(conn)

    # Close the connection
    conn.close()


if __name__ == '__main__':
    main()
"""
tasks_data = [
    {
        'title': 'Meeting with the marketing team',
        'description': 'Discuss the upcoming marketing campaigns and budget allocations.',
        'created_at': '2024-11-02 10:00:00',
        'status': False,
        'completed_at': None,
        'completed_by_id': None
    },
    {
        'title': 'Develop new feature for the app',
        'description': 'Implement the user authentication feature for the app.',
        'created_at': '2024-11-03 14:00:00',
        'status': False,
        'completed_at': None,
        'completed_by_id': None
    }
]


"""

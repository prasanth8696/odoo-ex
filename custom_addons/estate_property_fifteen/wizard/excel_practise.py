import xlwt





book = xlwt.Workbook()




sheet = book.add_sheet("invoice")

sheet.col(0).width = 256 * 5
sheet.col(1).width = 256 * 8
sheet.col(2).width = 256 * 4
sheet.col(3).width = 256 * 4
sheet.col(4).width = 256 * 4

sheet.col(6).width = 256 * 8
sheet.col(7).width = 256 * 4
sheet.col(8).width = 256 * 4
sheet.col(9).width = 256 * 4

sheet.col(10).width = 256 * 6
sheet.col(11).width = 256 * 6
sheet.col(12).width = 256 * 4
sheet.col(13).width = 256 * 5





style_1 = xlwt.easyxf('font: height 200, name Arial, colour_index black, bold on; align: horiz center;'  "borders: top thin, bottom thin, left medium ,right thin;")

style_2 = xlwt.easyxf('font: height 150, name Arial, colour_index black, bold on; align: horiz center;' "borders : right thin")
sheet.write_merge(2,3,0,13,'TAX INVOICE',style_1)

list = ['JAIN METAL ROLLING MILLS-OLD -UNIT II-old','PLOT NO: R1, R2, SIPCOT INDUSTRIAL COMPLEX, ,GUMMIDIPOONDI','TIRUVALLUR,601201']


for i in range(3) :
    sheet.write_merge((i + 4),(i + 4),0,13,list[i],style_2)
    

sheet.write_merge(7,7,0,13,'Phone: /Email: ',xlwt.easyxf('font: height 150, name Arial, colour_index black, bold on; align: horiz center;' "borders : right thin ,bottom thin"))

#set 1 
style_3 = xlwt.easyxf('font: height 150, name Arial, colour_index black; align: horiz left;' "borders : right thin ,bottom thin")
sheet.write_merge(8,9,0,1,' IRN',style_3)
list2 = [' GSTN NO',' State Code',' State Name',' PAN']
for index,value in enumerate(list2) :
    sheet.write_merge((10 + index),(10 + index),0,1,value,style_3)
    

    
#set 2
style_4 = xlwt.easyxf('font: height 150, name Arial, colour_index black, bold on; align: horiz left;' "borders : right thin,top thin,bottom thin")
sheet.write_merge(8,9,2,5,'44f835781007570adfba7a66e081cc2b68b2cb9a07cdaff079d28cbffa1a7de3',style_4)

list_3 = ['33AAAFJ4032F1Z0','33','TAMIL NADU']
for index,value in enumerate(list_3):
    sheet.write_merge((10 + index),(10 + index),2,5,value,style_4)
    
sheet.write_merge(13,13,2,4,'',style_4)
sheet.write(13,5,'',style_4)

    
 
 #set 3
sheet.write_merge(8,9,6,7,' Ack No.',style_3)
list2 = [' Invoice No',' Invoice Date',' PO Number',' PO Date']
for index,value in enumerate(list2) :
    sheet.write_merge((10 + index),(10 + index),6,7,value,style_3)
    
    
#set 4
sheet.write_merge(8,9,8,13,'152211732606187',style_4)

list_3 = ['JM/U2/3008/21-22','24/02/2022','OVER PHONE']
for index,value in enumerate(list_3):
    sheet.write_merge((10 + index),(10 + index),8,13,value,style_4)

sheet.write_merge(13,13,8,9,'',style_4)
sheet.write_merge(13,13,10,12,' Reverse Charge',style_3)
sheet.write(13,13,'N',style_4)

# set 5 and 6

list_4 = [' Name and Address of the Buyer','',' SHREE DEV TRADERS',' 47, CHINTHALAKUPPAM',' GUMMUDIPOONDI',' TAMIL NADU',' INDIA','',' GSTN: 33DDHPK8469L1ZW',' State Code: 33',' State: TAMIL NADU']

for index,value in enumerate(list_4) :
    if value == " SHREE DEV TRADERS" :
        sheet.write_merge((14 + index),(14 + index),0,5,value,style_4) 
        sheet.write_merge((14 + index),(14 + index),6,13,value,style_4)
        continue
         
    sheet.write_merge((14 + index),(14 + index),0,5,value,style_3) 
    sheet.write_merge((14 + index),(14 + index),6,13,value,style_3) 
    
#set 7 

list_5 = [' Transportation Mode',' Mode/Terms of Payments',' Vehicle No',' Place of Supply',' Date of Supply','']

for index,value in enumerate(list_5) :
        sheet.write_merge((25 + index),(25 + index),0,2,value,style_3) 
        
#set 8 ==>> set 7 values

list_6 = ['Road','','TN05R6354','GUMMIDIPOONDI','24/02/2022',''] 

for index,value in enumerate(list_6) :
            sheet.write_merge((25 + index),(25 + index),3,5,value,style_4)
            
            
            
#set 9 ==>> bank details

list_7 = [' Bank Name',' Branch',' Account No',' IFSC Code','']

sheet.write_merge(25,25,6,13,' Our Bank Details',xlwt.easyxf('font: height 150, name Arial, colour_index black, bold on; align: horiz center;' "borders : right thin ,top thin ,bottom thin "))

for index,value in enumerate(list_7) :
        sheet.write_merge((26 + index),(26 + index),6,7,value,style_3)
            
            
list_8 = ['','','','','']
for index,value in enumerate(list_8) :
        sheet.write_merge((26 + index),(26 + index),8,13,value,xlwt.easyxf('font: height 150, name Arial, colour_index black, bold on; align: horiz center;' "borders : right thin,top thin,bottom thin")
)


list_9 = ['SI NO',' Description and Specification of Goods','HSN CODE','UOM',' Quantity',' Rate',' Amount']

sheet.write(31,0,list_9[0], xlwt.easyxf('font: height 150, name Arial, colour_index black, bold on; align: horiz center;' "borders : right thin ,top thin ,bottom thin "))

sheet.write_merge(31,31,1,5,list_9[1],xlwt.easyxf('font: height 150, name Arial, colour_index black, bold on; align: horiz center;' "borders : right thin ,top thin ,bottom thin "))

sheet.write(31,6,list_9[2],xlwt.easyxf('font: height 150, name Arial, colour_index black, bold on; align: horiz center;' "borders : right thin ,top thin ,bottom thin "))

sheet.write(31,7,list_9[3],xlwt.easyxf('font: height 150, name Arial, colour_index black, bold on; align: horiz center;' "borders : right thin ,top thin ,bottom thin "))

sheet.write_merge(31,31,8,10,list_9[4],xlwt.easyxf('font: height 150, name Arial, colour_index black, bold on; align: horiz center;' "borders : right thin ,top thin ,bottom thin "))

sheet.write(31,11,list_9[5],xlwt.easyxf('font: height 150, name Arial, colour_index black, bold on; align: horiz center;' "borders : right thin ,top thin ,bottom thin "))

sheet.write_merge(31,31,12,13,list_9[6],xlwt.easyxf('font: height 150, name Arial, colour_index black, bold on; align: horiz center;' "borders : right thin ,top thin ,bottom thin "))


#table values 

list_10 = [['1','IRON SCRAP',"7204","kg",5760,34,195840]]

for index,item in enumerate(list_10):
        sheet.write(32+index,0,item[0],style_3)
        sheet.write_merge(32+index,32+index,1,5,item[1],style_3)
        sheet.write(32+index,6,item[2],style_3)
        sheet.write(32+index,7,item[3],style_3)
        sheet.write_merge(32+index,32+index,8,10,item[4],xlwt.easyxf('font: height 150, name Arial, colour_index black; align: horiz right;' "borders : right thin ,bottom thin"))
        sheet.write(32+index,11,item[5],xlwt.easyxf('font: height 150, name Arial, colour_index black; align: horiz right;' "borders : right thin ,bottom thin"))
        sheet.write_merge(32+index,32+index,12,13,item[6],xlwt.easyxf('font: height 150, name Arial, colour_index black; align: horiz right;' "borders : right thin ,bottom thin"))

        
sheet.write_merge(33,33,0,9,'Additional Info',style_3)
sheet.write_merge(34,39,0,9,"BEING SOLD IRON SCRAP FOR 5760.0 KGS VIDE OUR INV.NO. JM/U2/3008/21-22 DT.24-Feb-2022"
                  ,xlwt.easyxf('font: height 150, name Arial, colour_index black; align: horiz left,vert centre;' "borders : right thin ,bottom thin"))
sheet.write_merge(40,40,0,9,'Total Invoice Amount(In Words)',style_3)
sheet.write_merge(41,42,0,9,'Two Hundred And Thirty-One Thousand And Ninety-One Rupees and Twenty Paise',style_4)

list_11 = ['Taxable Amount','SGST','CGST','TCS 0.1%']
list_12 = [195840,17625.6,17625.6,0]

sheet.write_merge(33,34,10,11,list_11[0],style_4)
sheet.write_merge(33,34,12,13,list_12[0],style_4)
row = 35
for index in range(1,len(list_11)):
    sheet.write_merge(row,row,10,11,list_11[index],style_4)
    sheet.write_merge(row,row,12,13,list_12[index],style_4)
    row += 1
    
    
sheet.write_merge(38,39,10,11,'Total Tax Amount',style_4)
sheet.write_merge(38,39,12,13,35251.2,style_4)
sheet.write_merge(40,40,10,11,'Total Amount',style_4)
sheet.write_merge(40,40,12,13,231091.2,style_4)
sheet.write_merge(41,42,10,11,'',style_4)
sheet.write_merge(41,42,12,13,'',style_4)

list_13 = ['Terms of Sale','1.Goods once sold will not be taken back to exchanged',
            '2.Seller is not responsible for any loss or damaged of goods in transit',
            '3.Buyer undertakes to submit prescribed S.T.Dect to the seller on demand',
            '4.Dispute if any will be subject to seller\'s court jurisdiction.'
            
            ]


for index,value in enumerate(list_13):
    sheet.write_merge(43+index,43+index,0,5,value,style_3)


sheet.write_merge(43,43,6,13,'Certify that the particulars given above are true and Correct',xlwt.easyxf('font: height 150, name Arial, colour_index black; align: horiz right;' "borders : right thin ,bottom thin"))

sheet.write_merge(44,44,6,13,'FOR JAIN METAL ROLLING MILLS-OLD',xlwt.easyxf('font: height 150, name Arial, colour_index black,bold on; align: horiz right;' "borders : right thin ,bottom thin"))

sheet.write_merge(45,45,6,13,'')
sheet.write_merge(46,46,6,13,'')
sheet.write_merge(47,47,6,13,'AUTHORIZED SIGNATURE',xlwt.easyxf('font: height 150, name Arial, colour_index black, bold on; align: horiz right;' "borders : right thin ,bottom thin"))


sheet.write_merge(48,48,0,13,'SUBJECT TO CHENNAI JURISDICTION',xlwt.easyxf('font: height 150, name Arial, colour_index black, bold off; align: horiz center;'  "borders: top thin, bottom thin, left medium ,right thin;")
)





book.save("temp.xls")  
print("done")  
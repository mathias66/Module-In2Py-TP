Mathias = {
    'langagec':[13,20,15],
    'python' : [15,20,20],
    'sda'     :[15,16,17],
    'se'      :[17,18,19],
    'reseau'  :[17,18,20]
          }

moyenne = {
    'langagec' : (Mathias['langagec'][0]+Mathias['langagec'][1]+Mathias['langagec'][2])/3,
    'python' : (Mathias['python'][0]+Mathias['python'][1]+Mathias['python'][2])/3,
    'sda' : (Mathias['sda'][0]+Mathias['sda'][1]+Mathias['sda'][2])/3,
    'se' : (Mathias['se'][0]+Mathias['se'][1]+Mathias['se'][2])/3,
    'reseau' : (Mathias['reseau'][0]+Mathias['reseau'][1]+Mathias['reseau'][2])/3
}

List = list(range(1,11))

List[0]=List[0]+11
List[1]=List[1]+11
List[2]=List[2]+11
List[3]=List[3]+11
List[4]=List[4]+11
List[5]=List[5]+11
List[6]=List[6]+11
List[7]=List[7]+11
List[8]=List[8]+11
List[9]=List[9]+11

List.append(22)

ist.extend([23,24])

Listp = [List[0],List[2],List[4],List[6],List[8],List[10],List[12]]
ListI = [List[1],List[3],List[5],List[7],List[9],List[11]]

List.remove(List[3])


d={'nom':'Dupuis','prenom':'Jacques','age':30}

d.keys()
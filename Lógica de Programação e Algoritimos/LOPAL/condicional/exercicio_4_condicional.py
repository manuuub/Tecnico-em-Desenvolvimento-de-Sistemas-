ladoA=int(input("Digite o lado A:"))
ladoB=int(input("Digite o lado B:"))
ladoC=int(input("Digite o lado C:"))

if((ladoA+ladoB)>ladoC and (ladoA+ladoC)>ladoB and (ladoB+ladoC)>ladoA):
   if(ladoA==ladoB and ladoB == ladoC and ladoC==ladoA):
        print("Equilatero")
   elif(ladoA != ladoB and ladoB != ladoC and ladoC !=ladoA):
       print("Escaleno")
   else:
    print("Isósceles")
else:
  print("O triangulo não existe!")
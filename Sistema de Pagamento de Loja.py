print(' ====== LOJAS X ====== \n ')
compras = float(input('Total das compras: R$'))
print('\n FORMAS DE PAGAMENTO \n')
print(' [ 1 ] À vista (Desconto de 10%)\n'
      ' [ 2 ] Débito (Desconto de 5%)\n'
      ' [ 3 ] 2x no cartão (Sem juros) \n'
      ' [ 4 ] 3x ou mais (20% de Juros) \n')
pagamento = int(input('Informe a forma de pagamento que deseja: '))
if pagamento == 1:
    desconto1 = compras * 10 / 100
    print('\n ---- NOTA FISCAL ---- \n')
    print('SUBTOTAL: R${:.2f} \n'
          'DESCONTO APLICADO: 10% \n'
          'TOTAL: R${:.2f} \n'.format(compras, compras - desconto1))
    print('-'*23)
elif pagamento == 2:
    desconto2 = compras * 5 / 100
    print('\n ---- NOTA FISCAL ---- \n')
    print('SUBTOTAL: R${:.2f} \n'
          'DESCONTO APLICADO: 5% \n'
          'TOTAL: R${:.2f} \n'.format(compras, compras - desconto2))
    print('-'*23)
elif pagamento == 3:
    print('\n ---- NOTA FISCAL ---- \n')
    print('SUBTOTAL: R${:.2f} \n'
          'PARCELAS: 2x de R${:.2f} \n'
          'TOTAL: R${:.2f} \n'.format(compras, compras / 2 ,compras))
    print('-'*23)
elif pagamento == 4:
    parcelas = int(input('\nInforme a quantidade de parcelas: '))
    juros = compras * 20 / 100
    print('\n ---- NOTA FISCAL ---- \n')
    print('SUBTOTAL: R${:.2f} \n'
          'JUROS APLICADOS: 20% \n'
          'PARCELAS: {}x de R${:.2f} \n'
          'TOTAL: R${:.2f} \n'.format(compras, parcelas, (compras + juros) / parcelas, compras + juros))
    print('-'*23)
else:
    print('Opção inválida. Tente novamente!')
input('\nPressione ENTER para sair.')

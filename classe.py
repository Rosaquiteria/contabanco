import unittest

from unittest import main, TestCase


class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titu = titular
        self.saldo = saldo
        self.limite = limite
        self.operacoes = []

    def saque(self, valor=0):
        if valor <= self.limite + self.saldo:
            self.saldo -= valor
            self.operacoes.append(["Saque", valor])
            return True
        else:
            return False

    def deposito(self, valor):
        self.valor = valor
        if self.valor >= 10:
            self.saldo += valor
            self.operacoes.append(["Deposito", valor])

    def transfere(self, conta, valor):
        if self.saque(valor):
            conta.deposito(valor)
            self.operacoes.append(["Transfere", valor])
            return True
        else:
            return False

    def extrato(self):
        return self.saldo
        # print("CC Numero: %s" % self.numero)
        # for a in self.operacoes:
        #   print ("%-10s %10.2f" % (a[0], a[1]))

        #   print("Saldo \t %12.2f" % self.saldo)
        #   print("Lim. Especial \t %4.2f" % self.limite)
        #   print("Disponivel \t %8.2f" % int(self.limite + self.saldo)+"\n")


class ContaTestCase(unittest.TestCase):
    def setUp(self):
        self.conta = Conta(1, 'rosa', 20, 40)
        self.conta_2 = Conta(2, 'tais', 20, 40)

    def test_deposito(self):
        expected = 10

        self.conta.deposito(10)
        self.conta.saque(20)
        self.assertEqual(self.conta.saldo, expected)

    def test_saque(self):
        self.assertFalse(self.conta.saque(100))

    def test_extrato(self):
        self.assertEqual(self.conta.saldo, 20)

    def test_transferencia(self):
        self.conta.transfere(self.conta_2, 10)
        self.assertEqual(self.conta.saldo, 10)
        self.assertEqual(self.conta_2.saldo, 30)


if __name__ == '__main__':
    unittest.main()

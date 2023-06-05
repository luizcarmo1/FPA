import unittest
from unittest.mock import patch
from quebrando import *

def test_ler_usuarios(self):
    inputs = iter([
        '1' , '1965671' , '123' , '321'
    ])

class CadastroTest(unittest.TestCase):
    @patch('builtins.input', lambda _: '1')
    def test_qtde_alunos(self):
        self.assertEqual(ler_quantidade_alunos(), 1)
    
    @patch('builtins.input', lambda _: '1965671')
    def test_ler_ra(self):
        self.assertEqual(ler_ra(), '1965671')

    @patch('builtins.input', lambda _: '123')
    def test_ler_senha(self):
        self.assertEqual(ler_senha(), '123')

    @patch('builtins.input', lambda _: '321')
    def test_ler_senha(self):
        self.assertEqual(ler_pin(), '321')
    


class LoginPCTest(unittest.TestCase):
    def test_ler_alunos(self):
        ra = '1965671'
        pin = '321'
        inputs = iter([
            ra , pin
        ])
        with patch('builtins.input', lambda _ : next(inputs)):
            aluno = ler_aluno(senha = False)
            self.assertEqual(aluno.ra, ra)
            self.assertEqual(aluno.pin, pin)


class LoginAppTest(unittest.TestCase):
    def test_ler_aluno(self):
        ra = '1965671'
        senha = '123'
        pin = '321'
        inputs = iter([
            ra , senha , pin
        ])
        with patch('builtins.input', lambda _ : next(inputs)):
            aluno = ler_aluno()
            self.assertEqual(aluno.ra, ra)
            self.assertEqual(aluno.pin, pin)
            self.assertEqual(aluno.senha, senha)

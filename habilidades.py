from flask_restful import Resource

lista_habilidades = ['Python', 'Java', 'JavaScript', 'C/C++', 'PHP']


class Habilidades(Resource):
    def get(self):
        return lista_habilidades

from django.contrib import admin

from .models import Autor, Genero, Editora, Livro, Usuario, Emprestimo, Reserva, Multa

admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Editora)
admin.site.register(Livro)
admin.site.register(Usuario)
admin.site.register(Emprestimo)
admin.site.register(Reserva)
admin.site.register(Multa)

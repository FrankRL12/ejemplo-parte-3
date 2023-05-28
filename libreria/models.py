from django.db import models


class Estudiante(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10)
    ine = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    carrera = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    estado = models.CharField(max_length=10, choices=(('Activo', 'Activo'), ('Inactivo', 'Inactivo')))
    class Meta:
        verbose_name_plural = 'Estudiantes'
        verbose_name = 'Estudiante'
        ordering = ['-id']
    def __str__(self):
        return self.nombre


class Prestamo(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    libro = models.ForeignKey('Libro', on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField()
    cantidad = models.PositiveIntegerField()
    observacion = models.TextField()
    estado = models.CharField(max_length=10, choices=(('Activo', 'Activo'), ('Inactivo', 'Inactivo')))
    class Meta:
        verbose_name_plural = 'Prestamos'
        verbose_name = 'Prestamo'
        ordering = ['-id']

    

class Materia(models.Model):
    id = models.AutoField(primary_key=True)
    materia = models.CharField(max_length=100)
    estado = models.CharField(max_length=10, choices=(('Activo', 'Activo'), ('Inactivo', 'Inactivo')))
    class Meta:
        verbose_name_plural = 'Materias'
        verbose_name = 'Materia'
        ordering = ['-id']
    def __str__(self):
        return self.materia
    

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    autor = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='autores/')
    estado = models.CharField(max_length=10, choices=(('Activo', 'Activo'), ('Inactivo', 'Inactivo')))
    


    class Meta:
        verbose_name_plural = 'Autores'
        verbose_name = 'Autor'
        ordering = ['-id']
    def __str__(self):
        return self.autor
    


class Editorial(models.Model):
    id = models.AutoField(primary_key=True)
    editorial = models.CharField(max_length=100)
    estado = models.CharField(max_length=10, choices=(('Activo', 'Activo'), ('Inactivo', 'Inactivo')))
    class Meta:
        verbose_name_plural = 'Editoriales'
        verbose_name = 'Editorial'
        ordering = ['-id']
    def __str__(self):
        return self.editorial
    


class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='libros/')
    descripcion = models.TextField()
    estado = models.CharField(max_length=10, choices=(('Activo', 'Activo'), ('Inactivo', 'Inactivo')))
    class Meta:
        verbose_name_plural = 'Libros'
        verbose_name = 'Libro'
        ordering = ['-id']
    def __str__(self):
        return f"{self.titulo}"


class Configuracion(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    correo = models.EmailField(max_length=100)
    foto = models.ImageField(upload_to='fotos/')
    class Meta:
        verbose_name_plural = 'Configuraciones'
        verbose_name = 'Configuracion'
        ordering = ['-id']


class DetallePermiso(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=10, choices=(('Activo', 'Activo'), ('Inactivo', 'Inactivo')))
    permiso = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = 'Delle Permisos'
        verbose_name = 'Delle Permiso'
        ordering = ['-id']

    def __str__(self):
        return f'DetallePermiso #{self.id}'
    
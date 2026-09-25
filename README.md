# Gestión académica CampusLands

Aplicación de consola en **Python** para administrar el proceso académico de CampusLands. Maneja dos roles, coordinador y trainer, y guarda la información en archivos JSON.

Proyecto desarrollado en equipo por **Juan David Rivero Romero** y **María Bastilla**.

## Funcionalidades

**Coordinador**
- Inscribir y matricular campers, y registrar el resultado de su rendimiento
- Listar los campers en riesgo alto
- Añadir, eliminar y asignar trainers
- Administrar rutas de entrenamiento (Java, NetCore, NodeJS) y sus módulos
- Reportes: campers inscritos, aprobados en el examen inicial, con bajo rendimiento, trainers activos, campers y trainers por ruta, aprobados y desaprobados

**Trainer**
- Consultar su horario

## Estructura

| Archivo | Responsabilidad |
|---|---|
| `main.py` | Menú principal y navegación por roles |
| `CampersCRUD.py` | Inscripción y gestión de campers |
| `TrainersCRUD.py`, `TrainersHorario.py` | Gestión de trainers y horarios |
| `Modulonotas.py` | Registro de notas |
| `modulorutas.py` | Rutas de aprendizaje |
| `ModuloRalto.py` | Campers en riesgo alto |
| `ModuloReportes.py` | Reportes |
| `*.json` | Persistencia de datos |

## Cómo ejecutarlo

Requiere Python 3.

```bash
git clone https://github.com/juandariver9/Proyecto_Python_BastillaMaria-RomeroDavid.git
cd Proyecto_Python_BastillaMaria-RomeroDavid
python main.py
```

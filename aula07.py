import flet
from flet import (
          Checkbox,
          Column,
          FloatingActionButton,
          IconButton,
          OutlinedButton,
          Page,
          Row,
          Tab,
          Tabs,
          Text,
          TextField,
          UserControl,
          colors,
          icons,
  ) #importacao dos componentes que vao se usar na aplicacao

#Classe de tarefas
class Task(UserControl):
    def _init_(self, task_name, task_status_change, task_delete):
        super()._init_()
        self.completed = False
        self.task_name = task_name
        self.task_status_change = task_status_change
        self.task_delete = task_delete




#Classe da aplicacao toda
class Todoapp(UserControl):
    def build(self):
        self.new_task = TextField(
            hint_text = "Escreva a tarefa que deseja adicionar..."
            expand=True,
            on_submit=self.add_clicked,
        )
        self.task = Column()

        self.filter = Tabs(
            selected_index = 0,
            on_change = self.tabs_changed,
            tabs=[Tab(text="Todas tarefas"), Tab(text="Tarefas ativas"), Tab(text="Tarefas completadas")]
        )

        return Column(
            widht= 600,
            controls= [
                #Titulo da aplicacao
                Row([Text(value="tarefas",
                         style="headlineMedium")], alignment= "center"),
                Row(
                    #Input das tarefas
                    controls = [
                        self.new_task,
                        FloatingActionButton(icon=icons.ADD, on_click = self.add_clicked()),
                    ],
                ),
                Column(
                    Spacing=20,
                    controls=[
                        self.filter,
                        self.task,
                        Row(
                            alignment= "spaceBetween",
                            vertical_alignment="center",
                            controls=[
                                self.items_left,
                                OutlinedButton(
                                    text="Limpar as tarefas completadas".upper(),
                                    on_click=self.clear_clicked,
                                )

                            ]
                        )
                    ]
                )
            ]
        )

     def add_clicked(self):
         pass

def main(page: Page):
    page.tittle = "Tarefas"
    page.horizontal_alignment = "center"
    page.scroll = "adaptive"
    page.update()

#instancia a class principal
    app = Todoapp()


#sdicionando a aplicacao na pagina
    page.add(app)
    pass

flet.app(target=main)
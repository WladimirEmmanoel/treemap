import tkinter as tk

class TimeInfo:
    #Informaçoes do time
    def __init__(self, nome, splits, titulos):
        self.nome = nome
        self.splits = int(splits)
        self.titulos = int(titulos)

    #Retorna a cor verde baseada no número de títulos.
    def get_cor(self):
        tons_verdes = {1: '#00FF00', 2: '#00D900', 3: '#00B300', 4: '#009900', 5: '#007F00'}
        return tons_verdes[min(max(self.titulos, 1), 5)]

    # Retorna a proporção das vitórias em relação ao total
    def get_proporcao(self, total_splits):
        return self.splits / total_splits

class Treemap:
    #Cria e exibe o treemap dos times no canvas com o tkinter
    def __init__(self, root):
        self.root = root
        self.root.title("Treemap CBLOL 2024")
        self.canvas = tk.Canvas(root, width=600, height=600)
        self.canvas.pack()

        # Dados dos times
        self.times = [
            TimeInfo('PaiN', '14', '3'), 
            TimeInfo('Keyd', '12', '2'), 
            TimeInfo('Red Canids', '10', '2'), 
            TimeInfo('Loud', '6', '4'), 
            TimeInfo('Los Grandes', '6', '0'),
            TimeInfo('Kabum', '14', '4'), 
            TimeInfo('Furia', '9', '0'), 
            TimeInfo('Fluxo', '6', '0'), 
            TimeInfo('Intz', '14', '5'), 
            TimeInfo('Libery', '8', '0'),
        ]
        
        self.total_splits = sum(time.splits for time in self.times)
        self.canvas_treemap()

    #Cria um retangulo com a cor e textos informados
    def canvas_retangulo(self, x, y, width, height, cor, texto, proporcao):
        self.canvas.create_rectangle(x, y, x + width, y + height, fill=cor, outline="black")
        self.canvas.create_text(x + width / 2, y + height / 2 - 10, text=texto)
        self.canvas.create_text(x + width / 2, y + height / 2 + 10, text=proporcao)

    def canvas_treemap(self):
        x, y = 0, 0
        width_atual = 600
        height_atual = 600
        horizontal = True

        for time in self.times:
            proportion = time.get_proporcao(self.total_splits)
            area = proportion * 600 * 600

            if horizontal:
                retangulo_width = area / height_atual
                retangulo_height = height_atual
                self.canvas_retangulo(x, y, retangulo_width, retangulo_height, time.get_cor(), time.nome, f"{proportion:.1%}")
                x += retangulo_width
                width_atual -= retangulo_width
            else:
                retangulo_height = area / width_atual
                retangulo_width = width_atual
                self.canvas_retangulo(x, y, retangulo_width, retangulo_height, time.get_cor(), time.nome, f"{proportion:.1%}")
                y += retangulo_height
                height_atual -= retangulo_height

            horizontal = not horizontal

root = tk.Tk()
app = Treemap(root)
root.mainloop()

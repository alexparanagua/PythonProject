#existe plyer, notify-py, pynotifier, win10toast(win) etc...
import notifypy

def notifica(titulo: str, msg : str):
    notificacao = notifypy.Notify(enable_logging=True)
    notificacao.application_name = 'Notificacao Notify-py'
    notificacao.title = titulo
    notificacao.message=msg
    notificacao.urgency = 'critical' # low, normal or critical
    notificacao.audio='example.wav'
    notificacao.icon='example.png'

    notificacao.send(block=False)

notifica("teste de notificacao", "testando o notify-py para notificacao no SO")

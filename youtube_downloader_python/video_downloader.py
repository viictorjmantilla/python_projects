""" Modulos para descargar video en youtube """
import yt_dlp
import os

""" Funcion para medir el progreso de la descarga de los videos """
def progreso_descarga(d):
    """Muestra el progreso de la descarga en la terminal."""
    if d['status'] == 'downloading':
        porcentaje = d.get('_percent_str', '0%')
        velocidad = d.get('_speed_str', 'N/A')
        tiempo = d.get('_eta_str', 'N/A')
        print(f"\r🔽 {porcentaje} - 📡 {velocidad} - ⏳ ETA: {tiempo}", end="", flush=True)
           
""" Funcion para descargar videos basado en un enlace url """
def descargar_video(url, save_path):
    """Descarga un video de YouTube con barra de progreso y manejo de errores."""
    try:
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        opciones = {
            'outtmpl': f"{save_path}/%(title)s.%(ext)s",
            'progress_hooks': [progreso_descarga],
            'noplaylist': True,
            'quiet': True
        }

        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])

        print(f"\n✅ Descarga completada de la url: {url}")
    except yt_dlp.utils.DownloadError:
        print("\n❌ Error: La URL es inválida o el video no está disponible.")
    except PermissionError:
        print("\n❌ Error: No tienes permisos para guardar en esta carpeta.")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")

if __name__ == "__main__":
    
    save_path = r"C:\\Users\\Vic\Documents"
    videos_for_download = []
    
    while True:
        url_video = input("🔗 Ingresa la URL del video o ingrese 'Salir' para cerrar el programa: ").strip()
        
        if url_video.lower() == 'salir':
            print("")
            print("A continuacion se comenzaran a descargar los videos...")
            break
        else:
            videos_for_download.append(url_video)
        
    for video in videos_for_download:
        descargar_video(video, save_path)
        

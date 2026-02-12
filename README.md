Perfeito, Gabriel. Vou atualizar sua documentação considerando a integração com o projeto do vídeo (ESP32-CAM transmitindo via Wi-Fi), transformando seu sistema em:

📡 ESP32-CAM → Stream RTSP/HTTP → Python (face_recognition) → Controle de presença

Abaixo está a documentação atualizada e pronta para colocar no README do GitHub.

⸻

📹 Sistema de Presença com Reconhecimento Facial + ESP32-CAM

📌 Descrição do Projeto

Este projeto utiliza visão computacional e reconhecimento facial para rastrear automaticamente a presença dos alunos a partir de uma transmissão ao vivo gerada por uma ESP32-CAM.

A câmera transmite vídeo via rede Wi-Fi, e o script em Python captura esse stream em tempo real para:
	•	Detectar rostos
	•	Reconhecer alunos previamente cadastrados
	•	Calcular o tempo de permanência na aula
	•	Determinar presença com base em um limite mínimo (80%)

Ao final da sessão, o sistema exibe um relatório de presença com o tempo acumulado de cada aluno.

⸻

🏗 Arquitetura do Sistema

ESP32-CAM
     ↓ (Wi-Fi Stream)
Rede Local
     ↓
Python (OpenCV + face_recognition)
     ↓
Processamento em tempo real
     ↓
Relatório de presença


⸻

🔎 Visão Geral do Funcionamento

O script principal em Python executa as seguintes tarefas:
	•	Conecta-se ao stream de vídeo da ESP32-CAM.
	•	Carrega e codifica rostos conhecidos armazenados na pasta Faces/.
	•	Processa o vídeo em tempo real:
	•	Redimensiona o frame para otimizar desempenho.
	•	Converte o frame para RGB.
	•	Detecta rostos.
	•	Gera codificações faciais.
	•	Compara com os rostos conhecidos.
	•	Desenha retângulos e exibe nomes.
	•	Mantém um controle acumulado:
	•	Tempo total da aula.
	•	Tempo visível de cada aluno.
	•	Ao final da sessão:
	•	Calcula a porcentagem de presença.
	•	Marca como presente alunos visíveis por pelo menos 80% do tempo.

⸻

📡 Integração com ESP32-CAM

1️⃣ Configuração da ESP32-CAM

Utilize o exemplo:

Arquivo → Exemplos → ESP32 → Camera → CameraWebServer

Configure:

const char* ssid = "SEU_WIFI";
const char* password = "SUA_SENHA";

Selecione a placa:

AI Thinker ESP32-CAM

Após upload, o Serial Monitor mostrará um IP, por exemplo:

http://192.168.0.105

O stream normalmente estará disponível em:

http://192.168.0.105:81/stream


⸻

🧠 Código Python para Capturar Stream da ESP32-CAM

Substitua a fonte de vídeo:

import cv2

stream_url = "http://192.168.0.105:81/stream"
cap = cv2.VideoCapture(stream_url)

Agora o sistema processará o vídeo ao vivo da ESP32-CAM.

⸻

📂 Estrutura do Projeto

face-recognition-attendance/
│
├── face_cam.py
├── Faces/
│   ├── 550788.jpeg
│   ├── 123456.jpeg
│
├── requirements.txt
└── README.md


⸻

🚀 Funcionalidades
	•	✅ Reconhecimento facial em tempo real via Wi-Fi
	•	✅ Integração com ESP32-CAM
	•	✅ Cálculo automático de presença
	•	✅ Interface com anotação visual ao vivo
	•	✅ Processamento otimizado (redução de escala do frame)

⸻

⚙️ Instalação

1️⃣ Clone o repositório

git clone https://github.com/GabrielDiegues/Facial-Recognition.git
cd face-recognition-attendance

2️⃣ Crie ambiente virtual

python -m venv venv

Ative:

Windows:

venv\Scripts\activate

macOS/Linux:

source venv/bin/activate

3️⃣ Instale dependências

pip install opencv-python face_recognition numpy

⚠️ A biblioteca face_recognition pode exigir CMake e compiladores C++.

⸻

▶️ Como Usar
	1.	Coloque as imagens de referência na pasta Faces/.
	2.	Nomeie cada imagem com o RM do aluno.
	3.	Atualize o dicionário students_data.
	4.	Atualize a variável stream_url com o IP da ESP32-CAM.
	5.	Execute:

python face_cam.py

	6.	Pressione q para encerrar a sessão.
	7.	O relatório de presença será exibido no console.

⸻

🧮 Como o Cálculo de Presença Funciona

O sistema mede:

tempo_visivel_aluno / tempo_total_aula

Se o valor ≥ 0.8 (80%), o aluno é marcado como presente.

⸻

📊 Diferenças da Versão Anterior

Antes	Agora
Vídeo local (.mp4)	Stream ao vivo da ESP32-CAM
Uso offline	Monitoramento em tempo real
Testes simulados	Aplicação real em sala


⸻

🧠 Melhorias Futuras
	•	📦 Exportar relatório em CSV
	•	🗄 Integração com banco de dados
	•	🌐 Dashboard web
	•	🔔 Envio de notificações
	•	🧠 Reconhecimento com GPU
	•	🛡 Sistema multi-câmeras

⸻

📌 Requisitos
	•	Python 3.10+ (recomendado 3.10 ou 3.11)
	•	OpenCV
	•	face_recognition
	•	NumPy
	•	ESP32-CAM
	•	Rede Wi-Fi local

⸻

Agradecimentos
	•	face_recognition – Adam Geitgey
	•	OpenCV
	•	Projeto ESP32-CAM (AI Thinker)

⸻
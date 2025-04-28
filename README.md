# Grupo
- Gabriel Rocha | RM: 550788
- Luiza Cristina | RM: 99367
- Pedro Palladino | RM: 551180
- Renato Izumi | RM: 99242

# Sistema de Chamada com Reconhecimento Facial

Este projeto utiliza visão computacional e reconhecimento facial para rastrear automaticamente a presença dos alunos a partir de uma fonte de vídeo. Ele compara os rostos encontrados em um vídeo (ou transmissão ao vivo) com um conjunto de rostos conhecidos armazenados em uma pasta. O aplicativo exibe cada rosto reconhecido com um contorno e o nome correspondente do aluno. Ao final da sessão, calcula o tempo de presença de cada aluno e os marca como presentes se estiverem visíveis por pelo menos 80% do tempo total da aula.

## Visão Geral

Neste projeto, o script principal em Python executa as seguintes tarefas:

- Carrega um arquivo de vídeo pré-gravado (ou você pode modificá-lo para capturar vídeo ao vivo).
- Carrega e codifica rostos conhecidos a partir de imagens armazenadas na pasta `Faces/`. Os nomes dos arquivos (por exemplo, `550788.jpeg`) são usados para extrair um identificador único (RM) que mapeia para o nome do aluno em um dicionário de dados.
- Processa o vídeo quadro a quadro:
  - Inverte e redimensiona o quadro.
  - Converte o quadro para RGB.
  - Detecta a localização dos rostos e os codifica.
  - Compara os rostos detectados com os rostos conhecidos.
  - Desenha retângulos ao redor dos rostos detectados e exibe o nome correspondente.
- Mantém um total acumulado do tempo que o vídeo da aula foi reproduzido e contabiliza o tempo em que cada aluno reconhecido aparece.
- Ao final da sessão, calcula a proporção de presença de cada aluno. Um aluno é marcado como presente se aparecer em pelo menos 80% do tempo total da aula.
- Por fim, imprime um resumo de presença de cada aluno.

## Funcionalidades

- **Detecção e Reconhecimento Facial**: Utiliza a biblioteca `face_recognition` (que encapsula o dlib) para detectar e reconhecer rostos.
- **Rastreamento de Presença**: Registra o tempo em que cada aluno reconhecido aparece no vídeo.
- **Anotação em Tempo Real**: Desenha caixas delimitadoras e rótulos nos quadros do vídeo.
- **Loop de Reprodução do Vídeo**: Reinicia automaticamente o vídeo ao chegar ao final, útil para testes com vídeos pré-gravados.

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/GabrielDiegues/Facial-Recognition.git
   cd face-recognition-attendance
   ```

2. **Crie um ambiente virtual (recomendado):**

   ```bash
   python -m venv venv
   ```

3. **Ative o ambiente virtual:**

   - No Windows:
     ```bash
     venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Instale os pacotes necessários:**

   ```bash
   pip install opencv-python face_recognition numpy
   ```

   *Nota: A biblioteca `face_recognition` pode exigir CMake, dlib e ferramentas de compilação adicionais. Consulte a [página do GitHub do face_recognition](https://github.com/ageitgey/face_recognition) para solucionar problemas de instalação.*

## Como Usar

1. Coloque as imagens de referência dos rostos (nomeadas com o RM do aluno, por exemplo `550788.jpeg`) na pasta `Faces/`.

2. Atualize o dicionário `students_data` no script com os RMs e nomes dos alunos.

3. Execute o script com:

   ```bash
   python face_cam.py
   ```

4. O vídeo (por exemplo, `eu.mp4`) será reproduzido, e o sistema processará cada quadro, desenhando retângulos e nomes ao redor dos rostos reconhecidos.

5. Quando você pressionar **'q'**, o vídeo será interrompido. Nesse momento, o console exibirá os dados de cada aluno, incluindo se ele foi marcado como presente e o tempo correspondente de presença.

## Como Funciona

- **Captura de Vídeo**: Utiliza o `VideoCapture` do OpenCV para ler quadros de um arquivo de vídeo (ou de uma câmera ao vivo).
- **Codificação Facial**: Carrega imagens da pasta `Faces/` e usa `face_recognition.face_encodings()` para gerar uma impressão digital numérica de cada rosto.
- **Detecção de Rostos**: Para cada quadro do vídeo, o script encontra os rostos usando `face_recognition.face_locations()`.
- **Comparação de Rostos**: As codificações dos rostos detectados são comparadas com as codificações conhecidas usando `face_recognition.compare_faces()` e `face_recognition.face_distance()`.
- **Anotação**: O script desenha um retângulo ao redor do rosto e exibe o nome do aluno abaixo se o rosto for reconhecido.
- **Cálculo da Presença**: O script acumula a contagem de quadros para determinar por quanto tempo cada aluno esteve visível no vídeo, e calcula uma proporção de presença ao final.

## Requisitos

- Python 3.x (testado com Python 3.10; a compatibilidade com Python 3.12 pode exigir ajustes adicionais)
- OpenCV (`opencv-python`)
- face_recognition (e sua dependência, dlib)
- NumPy

## Agradecimentos

- [face_recognition](https://github.com/ageitgey/face_recognition) por Adam Geitgey  
- [OpenCV](https://opencv.org/)
```



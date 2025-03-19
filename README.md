# api-basica-com-img

    def upload_image(instance, filename):
        # Gera um nome único para o arquivo usando UUID
        file_extension = os.path.splitext(filename)[1]  # Obtém a extensão do arquivo (por exemplo, .jpg, .png)
        unique_filename = f"{uuid.uuid4()}{file_extension}"  # Cria um nome único para o arquivo
        return os.path.join('teste-arq', unique_filename)

->Esta função é um diferencial que além de criar automaticamnte um diretória dentro do sistema, também garante que
nenhuma imagem tenha o mesmo nome, assim a api não dará possíveis erros por causa da duplicação de nomes de imagens, também
vale observar que a imagem conserva sua exteção (ex: .jpg, .jpeg, .png, tec...)
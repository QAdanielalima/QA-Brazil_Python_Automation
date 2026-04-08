# 🚕 Automation Testing - Urban Routes Web App

## 📌 Project Overview

Projeto de automação de testes end-to-end desenvolvido em Python utilizando Selenium WebDriver, com foco na validação dos principais fluxos de um aplicativo web de rotas urbanas.

O **Urban Routes** é uma plataforma que permite ao usuário gerar rotas, estimar tempo e custo de viagens utilizando diferentes meios de transporte.

---

## 🎯 Objective

O objetivo deste projeto é validar, de forma automatizada, cenários críticos da aplicação, garantindo que funcionalidades essenciais estejam funcionando corretamente de forma rápida, confiável e repetível.

A automação foi pensada para:
- Reduzir esforço manual em testes repetitivos  
- Aumentar a confiabilidade das validações  
- Identificar defeitos que impactam a experiência do usuário  
- Criar uma base escalável para evolução dos testes  

---

## 🧪 Test Scope

A automação foi estruturada utilizando o padrão **Page Object Model (POM)**, garantindo melhor organização, reutilização de código e facilidade de manutenção.

Foram automatizados fluxos críticos da aplicação, incluindo:

- Preenchimento dos campos **"De"** e **"Para"**
- Seleção de corrida (chamar táxi)
- Inserção e validação de:
  - Número de telefone  
  - Código de confirmação  
  - Dados de pagamento (cartão)  
- Campo **"Deixar um comentário para o motorista"**
- Funcionalidade adicional: **Order Blanket**
- Validação da quantidade de itens selecionados (**Ice Cream**)
- Interação com o pop-up **"Buscar carro"**

Além disso, foram aplicadas boas práticas como:
- Uso de **localizadores robustos**
- **Explicit Waits** para sincronização
- Estrutura escalável para manutenção futura

---

## ⚙️ Test Environment
```
IDE: PyCharm
Framework: Pytest
Automação: Selenium WebDriver
Linguagem: Python
Browser: Google Chrome
Sistema Operacional: Windows 11
Tipo de Teste: End-to-End Automation
```
---

## 🛠️ Tools and Skills Applied

- Test Automation  
- Python  
- Selenium WebDriver  
- Pytest  
- Page Object Model (POM)  
- Explicit Waits  
- Checklists de Teste  
- Estruturação de cenários E2E  

---

## ▶️ Test Execution

Demonstração da execução dos testes automatizados:

No vídeo abaixo é possível visualizar os 8 cenários sendo executados automaticamente em poucos segundos, utilizando o Pytest e controlando o navegador via Selenium.

🔗 https://www.youtube.com/watch?v=eKnVDDAnyBw

---

## ✅ Results

A automação dos cenários críticos permitiu validar de forma rápida e confiável os principais fluxos da aplicação.

Testes que antes exigiriam execução manual repetitiva agora são executados em poucos segundos, proporcionando feedback rápido sobre a estabilidade do sistema.

Como resultado, o projeto entrega:

- Execução rápida e consistente dos testes  
- Redução de erros humanos durante validações  
- Maior cobertura dos fluxos críticos  
- Estrutura organizada e de fácil manutenção  
- Base pronta para expansão da automação  

---

## 💼 Business Impact

A automação de testes impacta diretamente a eficiência e a qualidade no desenvolvimento de software.

Com a execução automatizada, é possível identificar falhas mais cedo, reduzindo custos e evitando que problemas cheguem ao usuário final.

Principais benefícios:

- Redução do tempo de validação em cada release  
- Aumento da confiança nas entregas  
- Suporte a integração contínua (CI/CD)  
- Maior estabilidade do produto em produção  

Ao automatizar cenários críticos, as empresas conseguem escalar entregas com mais segurança, mantendo a qualidade sem comprometer a velocidade.

---

## 🚀 Final Considerations

Este projeto demonstra como a automação de testes vai além da execução técnica, contribuindo diretamente para a qualidade do produto e eficiência do processo de desenvolvimento.

A construção dessa suíte de testes reforça a importância de validar cedo, testar de forma inteligente e garantir valor contínuo para o usuário final.

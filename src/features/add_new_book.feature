#Som användare vill jag kunna lägga till en ny bok till min läslista så att jag kan hålla reda på vad jag vill läsa

  Feature: Lägga till en bok i läslistan
    Scenario:
      Given användaren navigerar till 'Lägg till bok'
      When användaren fyller i 'Titel'
      And användaren fyller i 'Författare'
      And användaren klickar på 'Lägg till ny bok' knappen
      Then boken läggs till som en ny rad i 'Katalog'
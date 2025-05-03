# Som testare vill jag att knappen 'Lägg till ny bok' ska vara inaktiv när fälten Titel eller Författare är tomma, så att användaren inte kan skapa en bok med ofullständig information.

  Feature: "Lägg till ny bok" knappen ska vara inaktiv om någon uppgift saknas
    Scenario:
      Given Användaren navigerar till "Lägg till bok"
      When Användaren fyller i Titel men inte Författare
      Then "Lägg till ny bok" knappen är inaktiv
      When Användaren fyller i Författare men inte Titel
      Then "Lägg till ny bok" knappen är inaktiv
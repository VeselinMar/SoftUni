function search() {
   let matchesCount = 0;
   let resultMatchesFound = document.getElementById('result');
   let townsList = document.getElementById('towns').getElementsByTagName('li');
   let searchText = document.getElementById('searchText').value;

   for (let i = 0; i < townsList.length; i++) {
      townsList[i].style.fontWeight = 'normal';
      townsList[i].style.textDecoration = 'none';
  }


   for (let i = 0; i < townsList.length; i++) {
      let townName = townsList[i].textContent;
      
      if (townName.includes(searchText)) {
          matchesCount++;
          townsList[i].style.fontWeight = 'bold';
          townsList[i].style.textDecoration = 'underline';
      }
  }

   resultMatchesFound.textContent = `${matchesCount} matches found`;
}

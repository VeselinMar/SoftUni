window.addEventListener("load", solve);

function solve() {
  // Get DOM elements
  const addContactButton = document.getElementById("add-btn");
  const contactName = document.getElementById("name");
  const contactNumber = document.getElementById("phone");
  const contactCategory = document.getElementById("category");
  const contactsList = document.getElementById("check-list");

  // Function to create a new contact entry
  function createContactEntry(name, phone, category) {
      const listItem = document.createElement("li");
      listItem.classList.add("contact");

      const article = document.createElement("article");
      article.classList.add("contact");

      const p1 = document.createElement("p");
      p1.textContent = `name:${name}`;

      const p2 = document.createElement("p");
      p2.textContent = `phone:${phone}`;

      const p3 = document.createElement("p");
      p3.textContent = `category:${category}`;

      article.appendChild(p1);
      article.appendChild(p2);
      article.appendChild(p3);

      listItem.appendChild(article);

      // Create edit and save buttons
      const saveAndEditButtonsContainer = document.createElement("div");
      saveAndEditButtonsContainer.classList.add("buttons");

      const editButton = document.createElement("button");
      editButton.classList.add("edit-btn");
      editButton.textContent = "Edit";

      const saveButton = document.createElement("button");
      saveButton.classList.add("save-btn");
      saveButton.textContent = "Save";

      saveAndEditButtonsContainer.appendChild(editButton);
      saveAndEditButtonsContainer.appendChild(saveButton);
      listItem.appendChild(saveAndEditButtonsContainer);

      // Edit button functionality
      editButton.addEventListener('click', () => {
          contactName.value = name;
          contactNumber.value = phone;
          contactCategory.value = category;
          listItem.remove();
      });

      // Save button functionality
      saveButton.addEventListener('click', () => {
          const contactList = document.getElementById("contact-list");
          contactList.appendChild(listItem);
          saveAndEditButtonsContainer.style.display = "none";

          // Create delete button for saved contact
          const deleteButton = document.createElement("button");
          deleteButton.classList.add("del-btn");
          deleteButton.textContent = "Delete";
          listItem.appendChild(deleteButton);

          // Delete button functionality
          deleteButton.addEventListener('click', () => {
              listItem.remove();
          });
      });

      return listItem;
  }

  // Add contact button click event listener
  addContactButton.addEventListener('click', () => {
      if (contactName.value !== '' && contactNumber.value !== '' && contactCategory.value !== '') {
          const newContact = createContactEntry(contactName.value, contactNumber.value, contactCategory.value);
          contactsList.appendChild(newContact);

          // Clear input fields
          contactName.value = '';
          contactNumber.value = '';
          contactCategory.value = '';
      }
  });
}

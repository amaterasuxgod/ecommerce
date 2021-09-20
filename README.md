### Host link: https://ecommerce-purified.herokuapp.com/home/homepage/

#### Unfortunately, i wasnt been able to host media files on aws cause i cant get a confirmation code on my phone:(

#### Home page structure:
1. Header consists of 2 sections which is a top section and a bottom section. In the top section there is a dropdown menu, from which you can choose whether you want to get
an info about delivery or payment.
In the bottom section there is a logo of the company and category menu on the left side. On the right side there is a serch icon, profile icon and basket icon. When switching
to the lower resolutions top section dissapears.

2. Main section consists of 2 subsections. On the first subsection there is a slider with a timer and on the second subsection there are product cards. When switching to the 
lower resolutions slider dissapears and product card that has no space available goes on a new row.

3. Footer basically consists of the company logo, featured products from the different categories and some company info. Just like in the main section, if there is not enough
space for the section it goes on a new line.

#### Product detail structure: 
Product detail page inherits from the main template, so there is the same header and footer as on the home page. But i decided to include subheader in order to switch between
different sections on the page. So, basically when clicking on "Описание" page switches to the description, by clicking on "Характеристики" page switches to the specifications
section. And by clicking on "Отзывы" page links the user to the reviews page, but only in case the user is authenticated. On the right side of the subheader there is a product
price. When the resolution gets lower, subheader turns into a dropdown.

Main section consists of 2 sections. In the first section,
on the left side there are pictures of a product(you can switch between them), on the right side there is a product title, product description, product price and the button for adding an item into a basket.
The more you click the button - the more items will be added into the busket.

In a second section there is a huge dropdown button and the subsection with reviews. By clicking on the button the list of specifications opens. If there are any reviews on the product-
they are displayed in the reviews section. 

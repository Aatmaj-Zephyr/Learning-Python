# [Learning Python- Intermediate course: Day 18, Tkinter — Types of Widgets part 1](https://dev.to/aatmaj/learning-python-intermediate-course-day-18-tkinter-types-of-widgets-part-1-2i6h)

Originally published on the dev.to platform [here](https://dev.to/aatmaj/learning-python-intermediate-course-day-18-tkinter-types-of-widgets-part-1-2i6h)

## Today we will explore widgets in Tkinter

---

> **Recap** Tkinter is the inbuilt python module that is used to create GUI applications. It is one of the most commonly used modules for creating GUI applications in Python as it is simple and easy to work with. For more information about Tkinter and it's advantages, please check out the [previous part](https://dev.to/aatmaj/learning-python-intermediate-course-day-17-tkinter-a-fast-and-easy-way-to-create-gui-applications-1if) of the course.

---

#### What are widgets?

> **Defination** A software widget is a relatively simple and easy-to-use software application or component made for one or more different software platforms.

In simple words, widgets are graphical elements like buttons, frames, textboxes etc. which are helpful in taking input from the user in graphical format. In Tkinter, Widgets are objects, that is they are instances of classes that represent buttons, frames, and so on. To make concepts simpler, just as we had treated strings and dictionaries, we can treat widgets too as as a 'button data type'. So the widgets have some data and have some methods to process that data.

#### Types of widgets

There are a lot of GUI widgets, both fancy and simple ones. (You can check out this [wiki link](https://en.wikipedia.org/wiki/Graphical_widget#List_of_common_generic_widgets) for a complete description) However there are some 18 widgets which are supported by Tkinter and are of a real significance.

##### Let us now check out all the widgets one by one

- Button
  Our plain old button. Python allows us to set the look and feel of the button.
  ![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/2okqndespmb6ywwkl5g0.png)

- Canvas
  The canvas widget adds graphics to the window. It can be used to draw graphs in the application.
  ![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/u7pbj99y3i6vq6bk6wpq.png)

- Checkbox
  Checkbox (or check-button) is an on-off type of button. The user can give binary inputs by clicking the button on or clicking the button off. The user can select one or all choices from the available list.
  ![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/38pj9fjjc48vdmwi7jkn.png)

- Radiobutton
  The Radiobutton also is an on-off type of button, but the user can only select one (and only one) out of the all available choices.
  ![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/m0mpo6fbfkdtjdvol3pr.png)

### Checkboxes vs. Radio Buttons

Checkbox allows one or many options to be selected. It is used when you want to allow user to select multiple choices. A radio button is used when you want to select only one option out of several available options. It is used when you want to limit the users choice to just one option from the range provided.

> Radio buttons are used when there is a list of two or more options that are mutually exclusive and the user must select exactly one choice. In other words, clicking a non-selected radio button will deselect whatever other button was previously selected in the list.
> Checkboxes are used when there are lists of options and the user may select any number of choices, including zero, one, or several. In other words, each checkbox is independent of all other checkboxes in the list, so checking one box doesn't uncheck the others.
> More on [Checkboxes vs. Radio Buttons By Nielsen Norman Group](https://www.nngroup.com/articles/checkboxes-vs-radio-buttons/)

---

## _To be continued....._

**Image credits**- All images in the text are my own screenshots.

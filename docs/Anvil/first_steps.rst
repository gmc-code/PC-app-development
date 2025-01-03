====================================================
First steps
====================================================

Do the tutorials
------------------------------

| Start at: https://anvil.works/learn/tutorials/feedback-form/chapter-1
| Work through the tutorials.
| Our own guide to the feedback form is at: https://pc-app-development.readthedocs.io/en/latest/Anvil/feedback_form.html

----

Become familiar with the docs
------------------------------

| Read: https://anvil.works/docs/editor
| Read: https://anvil.works/docs/client/quickstart
| Read: https://anvil.works/docs/client/ui
| Read: https://anvil.works/docs/client/components

| For publishing the app: https://anvil.works/docs/deployment-new-ide/quickstart#quickstart-deployment

----

As you use components:
------------------------------

| See the index to components in the anvil module: https://anvil.works/docs/api/anvil

-----

useful tips:
------------------------------

| In Code view, you can see that each Form is represented by a Python class.
| Its attributes and methods define how the app behaves.

| Code is auto-generated by the Anvil Editor when you add a new Form.
| Code is auto-generated by the Anvil Editor when you double click a button.

| Each component has an auto-generated name (e.g. self.button_1) which can be changed.
| This lets you refer to this component as an instance attribute in your Form class.
| e.g. self.text_box_1.text will return the text in the text box named text_box_1.

| Components placed side by side on the same row are separated by a draggable blue column separator.
| This column separator is visible when a component from that row is selected.
| Holding ctrl while dragging the separator allows for fine control.
| Double-clicking on the separator will reset all column widths from that row back to the default equal spacing.

| Next to each event, you can enter the name of a Python method. That method will be called when the event occurs.

| In an object's property events panel, click the blue arrow button to go to the method that runs when the event occurs.
| If there is no method name in the box, an appropriate name will be chosen using the name of the component and the event: e.g. button_1_click.

| The web browser is a constrained environment, so you can't open a file in the browser.
| You can make function calls to and from your own Python environments using the Uplink.


"""Script to convert markdown files to jinja2 templates."""
from dataclasses import dataclass, field
import markdown
import os


@dataclass
class Project:
    """Data structure representing a project."""

    input_filename: str
    output_filename: str
    image: str = ""
    title: str = ""
    advisor: str = ""
    student: str = ""
    major: str = ""
    description: list = field(default_factory=lambda: [])
    button: str = ""

    def parse_markdown_file(self):
        """Parses a markdown file containing project information."""
        input_lines = []
        current_section = ""

        with open(self.input_filename, "r") as in_file:
            input_lines = in_file.readlines()

        for line in input_lines:
            if line.startswith("## "):
                current_section = line.strip().lstrip("## ")
            else:
                if line.strip() == "":
                    continue

                if current_section == "Image":
                    self.image = line.strip()
                if current_section == "Title":
                    self.title = line.strip()
                elif current_section == "Advisor":
                    self.advisor = line.strip()
                elif current_section == "Student":
                    self.student = line.strip()
                elif current_section == "Major":
                    self.major = line.strip()
                elif current_section == "Description":
                    self.description.append(line)
                elif current_section == "Button":
                    self.button = line.strip()

    def strip_p_tags(self, text):
        """Removes <p> tags from text."""
        return text.replace("<p>", "").replace("</p>", "")

    def write_jinja2_template(self):
        """Writes a jinja2 template containing project information."""
        with open(self.output_filename, "w") as out_file:
            out_file.write(f"<a class='image'>{self.image}</a>\n")
            out_file.write(f"<h2 class='h3'>{self.title}</h2>\n")

            if self.advisor != "":
                # The advisor field is written in markdown to take advantage of the simple syntax for links.
                # We don't want to render the <p> tags created by markdown(), so we use `strip_p_tags()`.
                out_file.write(
                    f"<h3 class='h4'>Advisor: {self.strip_p_tags(markdown.markdown(self.advisor))}</h3>\n"
                )

            out_file.write(
                # The student field is written in markdown to take advantage of the simple syntax for links.
                # We don't want to render the <p> tags created by markdown(), so we use `strip_p_tags()`.
                f"<h3 class='h4'>Student: {self.strip_p_tags(markdown.markdown(self.student))}</h3>\n"
            )

            if self.major != "":
                out_file.write(f"<h4 class='h5'>Major: {self.major}</h4>\n")
            out_file.write(markdown.markdown("\n".join(self.description)))
            out_file.write("\n")

            if self.button != "":
                out_file.write(f"<ul class='actions'><li>{self.button}</li></ul>\n")


if __name__ == "__main__":
    for file in os.listdir(
        os.path.join("website", "research", "templates", "markdown")
    ):
        target_directory = ["projects", "abstracts"]

        if file.endswith(".md"):
            if file.startswith("abstract"):
                directory_name = target_directory[1]
            else:
                directory_name = target_directory[0]

            filename, _ = os.path.splitext(file)
            project = Project(
                os.path.join(
                    os.getcwd(),
                    "website",
                    "research",
                    "templates",
                    "markdown",
                    file,
                ),
                os.path.join(
                    os.getcwd(),
                    "website",
                    "research",
                    "templates",
                    directory_name,
                    filename + ".j2",
                ),
            )
            project.parse_markdown_file()
            project.write_jinja2_template()

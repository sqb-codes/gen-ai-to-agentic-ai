from prompts.coding_prompt import coding_prompt
from services.llm_services import get_model
from parsers.output_parsers import output_parser

model = get_model()

coding_chain = (
    coding_prompt | model | output_parser
)


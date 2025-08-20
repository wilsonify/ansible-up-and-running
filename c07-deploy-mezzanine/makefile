env.enc:
	sops encrypt --age age1mg4zlx7p736nnrp7glt7gyd96s33kmy8wlck903m0srkkndeaawqrqfzek --encrypted-regex "PASSW|MAIL|KEY" --input-type dotenv .env > .env.enc

env.tmp:
	SOPS_AGE_KEY_FILE=/home/thom/.config/sops/age/keys.txt sops decrypt --input-type dotenv --output-type dotenv .env.enc > .env.tmp

promote:
	mv .env.tmp .env

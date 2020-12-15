# All environment currently have almost same configuration and can be modified with requirement
# Production : logging level in INFO
# Development/Pre-production : logging level in DEBUG

#export PARKING_SYSTEM_ENV=development
export PARKING_SYSTEM_ENV=production
#export PARKING_SYSTEM_ENV=pre-production


# shellcheck disable=SC2059
echo -e "Loaded Environment : $PARKING_SYSTEM_ENV \n"
eval arg1="$1"
eval arg2="$2"

if [[ $arg2 ]] ; then
  echo "Invalid arguments, only 1 argument can be given"
  exit 0
fi

# shellcheck disable=SC1072
if [[ $arg1 == "interactive" ]] ; then

        echo -e " -------- Starting Interactive Mode ------------- \n"
        python run.py --interactive
fi

if [[ $arg1 ]] ; then
        regexp="filepath="
        if [[ $arg1 =~ $regexp ]] ; then
              echo -e " -------- Generating results from file input ------------- \n"
              python run.py "--"$arg1""
        else
          echo "Please provide filepath"
        fi
fi

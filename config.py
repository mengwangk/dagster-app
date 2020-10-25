@solid(config_schema={"reverse": bool})
def sort_by_calories(context, cereals):
    sorted_cereals = sorted(
        cereals,
        key=lambda cereal: int(cereal["calories"]),
        reverse=context.solid_config["reverse"],
    )

    if context.solid_config["reverse"]:  # find the most caloric cereal
        context.log.info(
            "{x} caloric cereal: {first_cereal_after_sort}".format(
                x="Most", first_cereal_after_sort=sorted_cereals[0]["name"]
            )
        )
        return {
            "most_caloric": sorted_cereals[0],
            "least_caloric": sorted_cereals[-1],
        }
    else:  # find the least caloric cereal
        context.log.info(
            "{x} caloric cereal: {first_cereal_after_sort}".format(
                x="Least", first_cereal_after_sort=sorted_cereals[0]["name"]
            )
        )
        return {
            "least_caloric": sorted_cereals[0],
            "most_caloric": sorted_cereals[-1],
        }

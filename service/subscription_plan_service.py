from entity.category import Category
from entity.duration_unit import DurationUnit
from entity.plan_name import PlanName
from entity.subscription_plan import SubscriptionPlan


class SubscriptionPlanService:
    One_Month_Duration_Unit = 1
    Three_Month_Duration_Unit = 3

    Music_Personal_Amount = 100
    Music_Premium_Amount = 250

    Video_Personal_Amount = 200
    Video_Premium_Amount = 500

    Podcast_Personal_Amount = 100
    Podcast_Premium_Amount = 300

    FREE_Amount = 0

    def __init__(self):
        self.category_to_subscription_plan = {}
        self.__preload_data()

    def get_all_music_subscriptions(self):
        return self.category_to_subscription_plan[Category.MUSIC]

    def get_all_podcast_subscriptions(self):
        return self.category_to_subscription_plan[Category.PODCAST]

    def get_all_video_subscriptions(self):
        return self.category_to_subscription_plan[Category.VIDEO]

    def get_subscription_by_category_and_plan_type(self, category, plan_name):
        subscription_plans = self.category_to_subscription_plan[category]
        for plan in subscription_plans:
            if plan.name == plan_name:
                return plan

    def __preload_data(self):
        # music initialization
        music_free_subscription_plan = SubscriptionPlan(PlanName.FREE, DurationUnit.MONTH,
                                                        SubscriptionPlanService.One_Month_Duration_Unit,
                                                        Category.MUSIC, SubscriptionPlanService.FREE_Amount)

        music_personal_subscription_plan = SubscriptionPlan(PlanName.PERSONAL, DurationUnit.MONTH,
                                                            SubscriptionPlanService.One_Month_Duration_Unit,
                                                            Category.MUSIC,
                                                            SubscriptionPlanService.Music_Personal_Amount)

        music_premium_subscription_plan = SubscriptionPlan(PlanName.PREMIUM, DurationUnit.MONTH,
                                                           SubscriptionPlanService.Three_Month_Duration_Unit,
                                                           Category.MUSIC,
                                                           SubscriptionPlanService.Music_Premium_Amount)
        # podcast intialization
        podcast_free_subscription_plan = SubscriptionPlan(PlanName.FREE, DurationUnit.MONTH,
                                                          SubscriptionPlanService.One_Month_Duration_Unit,
                                                          Category.PODCAST, SubscriptionPlanService.FREE_Amount)

        podcast_personal_subscription_plan = SubscriptionPlan(PlanName.PERSONAL, DurationUnit.MONTH,
                                                              SubscriptionPlanService.One_Month_Duration_Unit,
                                                              Category.MUSIC,
                                                              SubscriptionPlanService.Podcast_Personal_Amount)

        podcast_premium_subscription_plan = SubscriptionPlan(PlanName.PREMIUM, DurationUnit.MONTH,
                                                             SubscriptionPlanService.Three_Month_Duration_Unit,
                                                             Category.PODCAST,
                                                             SubscriptionPlanService.Podcast_Premium_Amount)
        # video initialization
        video_free_subscription_plan = SubscriptionPlan(PlanName.FREE, DurationUnit.MONTH,
                                                        SubscriptionPlanService.One_Month_Duration_Unit,
                                                        Category.VIDEO, SubscriptionPlanService.FREE_Amount)

        video_personal_subscription_plan = SubscriptionPlan(PlanName.PERSONAL, DurationUnit.MONTH,
                                                            SubscriptionPlanService.One_Month_Duration_Unit,
                                                            Category.VIDEO,
                                                            SubscriptionPlanService.Video_Personal_Amount)

        video_premium_subscription_plan = SubscriptionPlan(PlanName.PREMIUM, DurationUnit.MONTH,
                                                           SubscriptionPlanService.Three_Month_Duration_Unit,
                                                           Category.VIDEO,
                                                           SubscriptionPlanService.Video_Premium_Amount)

        self.category_to_subscription_plan[Category.MUSIC] = [music_free_subscription_plan,
                                                              music_personal_subscription_plan,
                                                              music_premium_subscription_plan]
        self.category_to_subscription_plan[Category.PODCAST] = [podcast_free_subscription_plan,
                                                                podcast_personal_subscription_plan,
                                                                podcast_premium_subscription_plan]
        self.category_to_subscription_plan[Category.VIDEO] = [video_free_subscription_plan,
                                                              video_personal_subscription_plan,
                                                              video_premium_subscription_plan]

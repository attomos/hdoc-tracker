export type Tweet = {
  text: string;
  entities: Entities;
  created_at: string;
  public_metrics: PublicMetrics;
  conversation_id: string;
  id: string;
};

export type TweetTuple = [string, Tweet[]];

export type GroupedTweets = {
  [key: string]: Tweet[];
};

export type TweetResponse = {
  data: Tweet[];
};

export type Entities = {
  hashtags?: Hashtag[];
  urls?: TweetUrl[];
  day_list?: HdocDay[];
  modern_day_list?: ModernHdocDay[];
  src_list?: Src[];
  demo_list?: Demo[];
};

export type Hashtag = {
  start: number;
  end: number;
  tag: string;
};

export type TweetUrl = {
  start: number;
  end: number;
  url: string;
  expanded_url: string;
  display_url: string;
};

export type CustomEntityBase = {
  start: number;
  end: number;
};

export type HdocDay = CustomEntityBase & {
  day: string;
};

export type ModernHdocDay = CustomEntityBase & {
  day: string;
};

export type Src = CustomEntityBase & {
  src: string;
  fixed: boolean;
};

export type Demo = CustomEntityBase & {
  demo: string;
  fixed: boolean;
};

export type PublicMetrics = {
  retweet_count: number;
  reply_count: number;
  like_count: number;
  quote_count: number;
};

export type ExpandedEntities = {
  expandedDemoUrl: string;
  expandedSrcUrl: string;
};
